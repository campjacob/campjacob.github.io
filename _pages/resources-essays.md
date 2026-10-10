---
title: Academic Essays
layout: foundation
nav_group: resources
author_sidebar: true
permalink: /resources/essays/
---
{%- assign essays = "" | split: "" -%}
{%- for r in site.resources -%}{%- if r.path contains "/essays/" -%}{%- assign essays = essays | push: r -%}{%- endif -%}{%- endfor -%}
{%- assign essays = essays | sort: "date" | reverse -%}
{%- assign by_year = essays | group_by_exp: "e", "e.date | date: '%Y'" -%}

<article class="resources-list">

<header class="my-4">
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb small mb-2">
      <li class="breadcrumb-item"><a href="/resources/">Resources</a></li>
      <li class="breadcrumb-item active" aria-current="page">Academic Essays</li>
    </ol>
  </nav>
  <h1 class="fw-bolder">Academic Essays</h1>
  <p class="lead mb-1">Essays I wrote for my Ph.D. in Transformative Studies at the California Institute of Integral Studies. To browse them by course, see the <a href="/resources/#essays">Resources</a> page.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-feather-alt" aria-hidden="true"></i> {{ essays | size }} essays, newest first.</p>
</header>

{%- for year in by_year %}
<section class="my-4">
  <h2 class="h5 fw-bold mb-2">{{ year.name }}</h2>
  <div class="card shadow-sm">
    <ul class="list-group list-group-flush">
      {%- for e in year.items -%}
      {%- assign course = e["Course ID"] | strip -%}
      <li class="list-group-item d-flex justify-content-between align-items-baseline gap-2">
        <span><a href="{{ e.url | relative_url }}" class="text-decoration-none">{{ e.title | escape }}</a>{% if course != "" %} <span class="badge text-bg-light border ms-1">{{ course }}</span>{% endif %}</span>
        <small class="text-body-secondary text-nowrap">{{ e.date | date: "%b %-d" }}</small>
      </li>
      {%- endfor -%}
    </ul>
  </div>
</section>
{%- endfor %}

</article>
