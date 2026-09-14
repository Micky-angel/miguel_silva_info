# Proyecto NASA — web de Miguel

Sitio hecho con **Jekyll**. Tres pestañas:

1. **Inicio** — foto de la persona + descripción del proyecto NASA + botón de apoyo.
2. **Proyecto** — la información detallada del proyecto.
3. **Sobre mí** — el CV.

## ✏️ Cómo actualizar el contenido

Todo el texto está en archivos sencillos. No hace falta saber programar:

| Qué quieres cambiar | Archivo a editar |
|---------------------|------------------|
| Foto, título, descripción y botón de la portada | `index.html` (la parte de arriba, entre las líneas `---`) |
| Detalles del proyecto | `proyecto.md` |
| Tu CV | `sobre-mi.md` |
| Nombre del sitio y menú | `_config.yml` |
| Colores | `assets/css/style.css` (variables de arriba) |

**Cambiar la foto:** copia tu imagen en `assets/img/` y en `index.html`
cambia la línea `imagen:` por el nombre de tu archivo
(por ejemplo `imagen: /assets/img/miguel.jpg`).

## ▶️ Ver la web en tu computadora

```bash
bundle install      # solo la primera vez
bundle exec jekyll serve
```

Luego abre http://localhost:4000

> Nota: Jekyll necesita Ruby 2.7 o superior. Si `bundle install` da error,
> instala una versión más nueva de Ruby (por ejemplo con `brew install ruby`).

## 🚀 Publicar gratis en GitHub Pages

1. Sube esta carpeta a un repositorio de GitHub.
2. En el repositorio: **Settings → Pages → Build from branch → main**.
3. Si la URL queda como `usuario.github.io/pwebMiguel`, descomenta la línea
   `baseurl:` en `_config.yml` y pon el nombre del repositorio.
