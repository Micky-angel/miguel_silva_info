---
layout: default
title: Programa
permalink: /proyecto/
---

<span class="etiqueta">International Air and Space Program </span>


El **IASP (International Air and Space Program)** es una iniciativa educativa
en la que estudiantes y graduados de todo el mundo trabajan en proyectos
aeroespaciales reales junto a ingenieros y profesionales expertos de la NASA.


<div class="tarjeta" markdown="1">
### Actividades
- Entrenamiento astronáutico
- Experiencia de flotación neutra *(neutral buoyancy)*
- Pilotaje simulado
- Control de misión y roles de control de vuelo
- Caminatas espaciales (EVA), teóricas y prácticas
- Construcción de robótica lunar
- Desafíos tecnológicos científicos
- y más
</div>


<div class="tarjeta" markdown="1">
### Fui seleccionado por mi perfil de investigador en ingeniería espacial y robótica!
<div class="carta-fila">
<figure class="figura">
  <img src="{{ '/assets/img/carta.png' | relative_url }}" alt="Carta de selección IASP 2026">
</figure>
<div class="carta-texto" markdown="1">
Participaré en esta versión 2026 representando a Bolivia. El programa tiene un costo de $4,450 USD, el cual puede ser cubierto por empresas en calidad de sponsors. Uno de los beneficios consiste en la inclusión del logotipo de la empresa en el traje de vuelo (entre 4 a 7).
</div>
</div>
</div>



## Apoyo Recibido
Agradezco a todas las personas, redes de prensa y amigos que me han ayudado en la difusión de mi participación en este programa. También les agradezco profundamente por sus aportes voluntarios. Después del evento prepararé charlas y talleres para difundir esta experiencia con el fin de motivarles a que sean la próxima generación de bolivianos en este programa.


<!--
<div class="donaciones">

  <div class="col">
    <p class="col-titulo">Colaboradores</p>
    <div class="col-ventana">
      <ul class="track track-1">
        {% for n in site.data.donaciones.donantes %}<li>{{ n }}</li>{% endfor %}
        {% for n in site.data.donaciones.donantes %}<li>{{ n }}</li>{% endfor %}
      </ul>
    </div>
  </div>

  <div class="col">
    <p class="col-titulo"></p>
    <div class="col-ventana">
      <ul class="track track-2">
        {% for n in site.data.donaciones.grandes %}<li>{{ n }}</li>{% endfor %}
        {% for n in site.data.donaciones.grandes %}<li>{{ n }}</li>{% endfor %}
      </ul>
    </div>
  </div>

  <div class="col">
    <p class="col-titulo"></p>
    <div class="col-ventana">
      <ul class="track track-3 estatica">
        {% for n in site.data.donaciones.empresas %}<li>{{ n }}</li>{% endfor %}
      </ul>
    </div>
  </div>

</div>
-->!

## Brochure

<a class="boton menta" href="{{ '/assets/doc/brochure.pdf' | relative_url }}" target="_blank" rel="noopener">📄 Ver brochure (PDF)</a>

<iframe class="pdf-visor" src="{{ '/assets/doc/brochure.pdf' | relative_url }}" title="Brochure IASP 2026"></iframe>

## Sponsors

<div class="colaboradores">
  {% for c in site.data.colaboradores %}
  <div class="logo">
    {% if c.logo %}<img src="{{ c.logo | relative_url }}" alt="{{ c.nombre }}">{% else %}<span>{{ c.nombre }}</span>{% endif %}
  </div>
  {% endfor %}
</div>

<a class="boton menta-solido" href="{{ '/sobre-mi/' | relative_url }}">Sobre mí →</a>
