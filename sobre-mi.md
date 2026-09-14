---
layout: default
title: Sobre mí
permalink: /sobre-mi/
---

<span class="etiqueta">Currículum</span>

# Miguel Ángel Silva Plata

Estudiante de 9.º semestre de **Ingeniería Mecatrónica** en la Universidad
Católica Boliviana, con un fuerte enfoque en Electrónica y Sistemas de Control.
Actualmente Presidente del Capítulo Estudiantil IEEE Aerospace and Electronics
Systems Society. Contribuyo en investigaciones sobre sistemas de control de
satélites como líder de la división estudiantil del proyecto nacional apoyado
por la UNOOSA: **WASKIRI-SAT-BOLIVIA**. He publicado 6 artículos de
investigación en ingeniería mecatrónica y espacial (4 como autor principal y
2 como coautor), con experiencia en diseño, prototipado y construcción de
equipos robóticos, además de docencia académica.

<div class="tarjeta" markdown="1">
## Datos
- **Nombre:** Miguel Ángel Silva Plata
- **Nacionalidad:** Bolivia
- **LinkedIn:** [Miguel Ángel Silva](https://linkedin.com/in/miguel-angel-silva-plata/)
</div>

<div class="tarjeta" markdown="1">
## Educación
- **Pontificia Universidad Católica de Chile** — Santiago, Chile *(Mar 2026 – Jul 2026)*
  Seleccionado para el programa de intercambio estudiantil
- **Universidad Católica Boliviana "San Pablo" (UCB)** — La Paz, Bolivia *(Feb 2022 – Presente)*
  Estudiante de Ingeniería Mecatrónica. Ganador de la Beca Bachiller de Plata. GPA: 94/100.
- **Centro Boliviano Americano** — Diploma de dominio del idioma inglés *(Mar 2019 – Dic 2020)*
  Nivel C1. GPA: 90/100.
</div>

<div class="tarjeta" markdown="1">
## Experiencia académica y laboral
- **Presidente**, Capítulo Estudiantil IEEE Aerospace and Electronic Systems Society *(Ago 2025 – Presente)*
- **Pasante de Diseño Mecánico**, Maquintel Robotic Services — Santiago, Chile *(Mayo 2026-Agosto 2026)*
- **Vicepresidente**, Sociedad Científica Estudiantil de Ingeniería Mecatrónica — comunidad de +100 miembros *(Feb 2024 – Ene 2026)*
- **Pasante de Laboratorio**, INTILAB UCH — Lima, Perú *(Feb 2026)*
- **Pasante de Laboratorio**, FabLab UCHILE *(Jul 2024)*
- **Asistente de Investigación**, CIDIMEC *(Ago 2023 – Presente)*
- **Auxiliar de Docencia**: Circuitos I y II, Circuitos Digitales, Control I — UCB "San Pablo" *(Feb 2024 – Jul 2025)*
</div>

<div class="tarjeta" markdown="1">
## Investigaciones
6 artículos publicados en ingeniería mecatrónica y espacial, además de mis proyectos WASKIRI-SAT y Rover SALT.

<a class="boton-texto" href="{{ '/investigaciones/' | relative_url }}">Ver investigaciones y publicaciones</a>
</div>

<div class="tarjeta" markdown="1">
## Eventos y talleres
- Organizador de la Primera Semana **CONSTELACIÓN LATAM** con SGAC Latinoamérica.
- Delegado de Bolivia en el 10.º Taller de Generación Espacial Sudamericano SGAC 2026 (SA-SGW 2026), Santiago, Chile *(Abr 2026)*.
- Organizador del primer **Encuentro Aeroespacial Boliviano (AESSBAM)** — La Paz, Bolivia *(Dic 2025)*.
- Asistente al 9.º Taller de Generación Espacial Sudamericano SGAC 2025, Lima, Perú *(Nov 2025)*.
- Presentador de póster en el Encuentro Latinoamericano de IA **KHIPU**, Santiago, Chile *(Mar 2025)*.
- Voluntario y organizador en la conferencia científica IEEE ITEC UCB *(Oct 2023, 2024, 2025)*.
</div>

<div class="tarjeta" markdown="1">
## Premios y distinciones
- **2do premio nacional** INFOMATRIX (Nacional e Internacional, 2024–2025): Réplica física interactiva de un nanosatélite educativo y 3.er premio internacional por una interfaz de mapeo satelital para divulgación científica.
- **1er premio**, Rally Latinoamericano de Innovación *(Oct 2023)* — proyecto de reciclaje en hogares vulnerables (impacto social).
- **Múltiples medallas** en Olimpiadas Científicas nacionales *(2018–2021)* en programación, física y matemáticas.
</div>

<div class="tarjeta" markdown="1">
## Certificaciones
- Gestión de Proyectos para el Desarrollo — Banco Interamericano de Desarrollo (BID).
- Certificación de Coursera.
</div>

<div class="tarjeta" markdown="1">
## Tecnologías y habilidades
Robótica con ROS2 · Electrónica y diseño de PCB · Control Moderno · Visión Artificial ·
C++ y Python · Programación de microcontroladores · MATLAB · Fusion 360 y SolidWorks · Geogebra y Mathematica · Dibujo digital en Procreate.

**Deportes:** Tenis y Kung Fu.
</div>

## Galería

{% assign fotos = "1,2,3,4,5,6,7,8,9,10" | split: "," %}
<div class="galeria" style="--dur: {{ fotos | size | times: 3.5 }}s">
  {% for n in fotos %}
  <img src="{{ '/assets/img/galeria/miguel-' | append: n | append: '.jpg' | relative_url }}" alt="Miguel Ángel Silva {{ n }}" loading="lazy" style="animation-delay: {{ forloop.index0 | times: 3.5 }}s">
  {% endfor %}
</div>
