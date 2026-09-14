#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_preview.py  —  Previsualizador local del sitio (sin Ruby/Jekyll)

Renderiza las páginas del sitio (resolviendo el Liquid básico que usa Jekyll)
a la carpeta  _preview/  con rutas relativas, para poder abrirlas con DOBLE CLIC
en el navegador (file://), sin necesidad de servidor.

Uso:
    python build_preview.py
Luego abre:  _preview/index.html

Requisitos (una sola vez):
    python -m pip install markdown pyyaml
"""
import os, re, glob, datetime
import yaml
import markdown as md_lib

RAIZ = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(RAIZ, "_preview")

# ---- Mapa de rutas Jekyll -> archivo local dentro de _preview/ ----
URLMAP = {
    "/": "index.html",
    "/investigaciones/": "investigaciones.html",
    "/aexa-iasp/": "aexa-iasp.html",
    "/aess-bolivia/": "aess-bolivia.html",
    "/sobre-mi/": "sobre-mi.html",
    "/proyecto/": "aexa-iasp.html",  # ruta antigua -> nueva
}

def relative_url(path):
    """Convierte una ruta absoluta del sitio a una relativa para _preview/."""
    if not isinstance(path, str):
        return path
    if path in URLMAP:
        return URLMAP[path]
    if path.startswith("/"):
        return "../" + path[1:]   # assets, docs, imágenes...
    return path

# ==========================================================
#  Mini-motor de plantillas (subconjunto de Liquid usado aquí)
# ==========================================================
TOKEN = re.compile(r"(\{\%.*?\%\}|\{\{.*?\}\})", re.DOTALL)

def resolver(base, ctx):
    """Resuelve una ruta con puntos: 'page.url', 'c.logo', 'forloop.index0'."""
    base = base.strip()
    # literal string
    if (base.startswith('"') and base.endswith('"')) or (base.startswith("'") and base.endswith("'")):
        return base[1:-1]
    # número
    if re.fullmatch(r"-?\d+(\.\d+)?", base):
        return float(base) if "." in base else int(base)
    cur = ctx
    for parte in base.split("."):
        if isinstance(cur, dict):
            cur = cur.get(parte)
        else:
            cur = getattr(cur, parte, None)
        if cur is None:
            return None
    return cur

def num_fmt(n):
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    return str(n)

def aplicar_filtro(valor, nombre, args, ctx):
    if nombre == "relative_url":
        return relative_url(valor)
    if nombre == "default":
        return valor if (valor not in (None, "", False)) else args[0]
    if nombre == "date":
        # solo usamos el año
        return datetime.datetime.now().strftime(args[0]) if isinstance(valor, (datetime.datetime,)) else datetime.datetime.now().strftime(args[0])
    if nombre == "size":
        return len(valor) if valor is not None else 0
    if nombre == "times":
        return float(valor) * float(args[0])
    if nombre == "append":
        return (valor if valor is not None else "") + str(args[0])
    if nombre == "prepend":
        return str(args[0]) + (valor if valor is not None else "")
    if nombre == "split":
        return (valor or "").split(args[0])
    if nombre == "remove":
        return (valor or "").replace(args[0], "")
    if nombre == "downcase":
        return (valor or "").lower()
    if nombre == "replace":
        return (valor or "").replace(args[0], args[1])
    return valor

def parse_args(resto):
    """Parsea 'a', 'b'  o  ' ', '-'  o  3.5  tras ':' de un filtro."""
    args = []
    for a in split_top(resto, ","):
        a = a.strip()
        if not a:
            continue
        if (a[0] in "\"'") and (a[-1] == a[0]):
            args.append(a[1:-1])
        elif re.fullmatch(r"-?\d+(\.\d+)?", a):
            args.append(float(a) if "." in a else int(a))
        else:
            args.append(a)
    return args

def split_top(texto, sep):
    """split por 'sep' respetando comillas."""
    partes, actual, q = [], "", None
    for ch in texto:
        if q:
            actual += ch
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch; actual += ch
        elif ch == sep:
            partes.append(actual); actual = ""
        else:
            actual += ch
    partes.append(actual)
    return partes

def evaluar(expr, ctx):
    """Evalúa 'base | filtro: arg | filtro2' -> string."""
    trozos = split_top(expr, "|")
    valor = resolver(trozos[0], ctx)
    for f in trozos[1:]:
        f = f.strip()
        if ":" in f:
            nombre, resto = f.split(":", 1)
            args = parse_args(resto)
        else:
            nombre, args = f, []
        valor = aplicar_filtro(valor, nombre.strip(), args, ctx)
    return valor

def condicion(expr, ctx):
    expr = expr.strip()
    if "==" in expr:
        a, b = expr.split("==", 1)
        return str(evaluar(a, ctx)) == str(evaluar(b, ctx))
    if "!=" in expr:
        a, b = expr.split("!=", 1)
        return str(evaluar(a, ctx)) != str(evaluar(b, ctx))
    val = evaluar(expr, ctx)
    return val not in (None, "", False, 0)

def tokenizar(txt):
    return [t for t in TOKEN.split(txt) if t != ""]

def render(tokens, ctx):
    salida, i = [], 0
    while i < len(tokens):
        t = tokens[i]
        if t.startswith("{{"):
            expr = t[2:-2].strip()
            val = evaluar(expr, ctx)
            salida.append("" if val is None else num_fmt(val) if isinstance(val, (int, float)) else str(val))
            i += 1
        elif t.startswith("{%"):
            tag = t[2:-2].strip()
            palabra = tag.split()[0]
            if palabra == "assign":
                m = re.match(r"assign\s+(\w+)\s*=\s*(.+)", tag)
                ctx[m.group(1)] = evaluar(m.group(2), ctx)
                i += 1
            elif palabra == "for":
                m = re.match(r"for\s+(\w+)\s+in\s+(.+)", tag)
                var, itexpr = m.group(1), m.group(2)
                cuerpo, i = extraer(tokens, i + 1, "endfor")
                lista = evaluar(itexpr, ctx) or []
                for idx, item in enumerate(lista):
                    hijo = dict(ctx)
                    hijo[var] = item
                    hijo["forloop"] = {"index0": idx, "index": idx + 1,
                                       "first": idx == 0, "last": idx == len(lista) - 1}
                    salida.append(render(cuerpo, hijo))
            elif palabra == "if":
                cond = tag[2:].strip()
                bloque, i = extraer(tokens, i + 1, "endif")
                ramas = dividir_if(bloque)
                ramas[0] = (cond, ramas[0][1])   # la 1.ª rama usa la condición del if
                elegido = None
                for (ctag, cuerpo) in ramas:
                    if ctag is None:  # else
                        elegido = cuerpo; break
                    if condicion(ctag, ctx):
                        elegido = cuerpo; break
                if elegido:
                    salida.append(render(elegido, ctx))
            else:
                i += 1  # tags ignorados
        else:
            salida.append(t)
            i += 1
    return "".join(salida)

def extraer(tokens, i, cierre):
    """Devuelve (tokens_del_bloque, indice_tras_cierre) respetando anidación."""
    profundidad, bloque = 1, []
    aperturas = {"endfor": "for", "endif": "if"}[cierre]
    while i < len(tokens):
        t = tokens[i]
        if t.startswith("{%"):
            p = t[2:-2].strip().split()[0]
            if p == aperturas:
                profundidad += 1
            elif p == cierre:
                profundidad -= 1
                if profundidad == 0:
                    return bloque, i + 1
        bloque.append(t)
        i += 1
    return bloque, i

def dividir_if(tokens):
    """Divide un bloque if en ramas [(cond, cuerpo), ... , (None, else)]."""
    ramas, cond_actual, cuerpo, prof = [], "__first__", [], 0
    # el primer 'cond' lo maneja quien llama; aquí sólo separamos elsif/else de nivel 0
    ramas_tmp = [("__PRIMERA__", [])]
    for t in tokens:
        if t.startswith("{%"):
            p = t[2:-2].strip()
            w = p.split()[0]
            if w in ("for", "if"):
                prof += 1
            elif w in ("endfor", "endif"):
                prof -= 1
            if prof == 0 and w == "else":
                ramas_tmp.append((None, []))
                continue
            if prof == 0 and w == "elsif":
                ramas_tmp.append((p[5:].strip(), []))
                continue
        ramas_tmp[-1][1].append(t)
    return ramas_tmp

# ==========================================================
#  Carga de datos, páginas y layout
# ==========================================================
def cargar_yaml(ruta):
    with open(ruta, encoding="utf-8") as f:
        return yaml.safe_load(f)

def leer_front_matter(ruta):
    with open(ruta, encoding="utf-8") as f:
        txt = f.read()
    # El front matter va entre dos líneas que son exactamente '---'
    m = re.match(r"^---\s*\n(.*?)\n---[ \t]*\n?(.*)$", txt, re.DOTALL)
    if m:
        return yaml.safe_load(m.group(1)) or {}, m.group(2).lstrip("\n")
    return {}, txt

def main():
    # Config y datos
    site = cargar_yaml(os.path.join(RAIZ, "_config.yml")) or {}
    site["time"] = datetime.datetime.now()
    site["data"] = {}
    ddir = os.path.join(RAIZ, "_data")
    if os.path.isdir(ddir):
        for y in glob.glob(os.path.join(ddir, "*.yml")):
            site["data"][os.path.splitext(os.path.basename(y))[0]] = cargar_yaml(y)

    with open(os.path.join(RAIZ, "_layouts", "default.html"), encoding="utf-8") as f:
        layout = f.read()
    layout_tokens = tokenizar(layout)

    # Páginas: index.html + *.md con front matter que tenga 'layout'
    candidatos = [os.path.join(RAIZ, "index.html")] + glob.glob(os.path.join(RAIZ, "*.md"))
    os.makedirs(SALIDA, exist_ok=True)
    generadas = []

    for ruta in candidatos:
        fm, cuerpo = leer_front_matter(ruta)
        if "layout" not in fm:
            continue
        base = os.path.basename(ruta)
        es_md = base.endswith(".md")
        salida_nombre = "index.html" if base == "index.html" else os.path.splitext(base)[0] + ".html"

        # URL de la página (para marcar el menú activo)
        page = dict(fm)
        page["url"] = fm.get("permalink", "/")

        ctx = {"site": site, "page": page}

        # 1) Renderiza Liquid del cuerpo
        cuerpo_html = render(tokenizar(cuerpo), ctx)
        # 2) Si es markdown, conviértelo a HTML
        if es_md:
            cuerpo_html = md_lib.markdown(
                cuerpo_html,
                extensions=["extra", "md_in_html", "sane_lists"],
            )
        # 3) Inserta en el layout
        ctx_layout = {"site": site, "page": page, "content": cuerpo_html}
        html = render(list(layout_tokens), ctx_layout)

        with open(os.path.join(SALIDA, salida_nombre), "w", encoding="utf-8") as f:
            f.write(html)
        generadas.append(salida_nombre)

    print("Previsualización generada en:  _preview/")
    for g in generadas:
        print("   -", g)
    print("\nAbre con doble clic:  _preview/index.html")

if __name__ == "__main__":
    main()
