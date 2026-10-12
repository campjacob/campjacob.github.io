---
title: Sitemap
layout: page_foundation
permalink: /sitemap/
author_profile: true
---

{%- comment -%}
Every page on the site, grouped. Resources are grouped by their folder (as on /resources/), blog posts by year.
The page list is written out here; add a page to it when you make a new one.
{%- endcomment -%}
{%- assign essays = "" | split: "" -%}{%- assign articles = "" | split: "" -%}{%- assign informationals = "" | split: "" -%}
{%- for r in site.resources -%}
  {%- if r.path contains "/essays/" -%}{%- assign essays = essays | push: r -%}
  {%- elsif r.path contains "/articles/" -%}{%- assign articles = articles | push: r -%}
  {%- else -%}{%- assign informationals = informationals | push: r -%}{%- endif -%}
{%- endfor -%}
{%- assign essays = essays | sort: "title" -%}{%- assign articles = articles | sort: "title" -%}{%- assign informationals = informationals | sort: "title" -%}
{%- assign groups = "Main|Home:/,Blog:/blog/,Resources:/resources/,Projects:/projects/,Curriculum Vitae:/cv/,Contact:/contact/,About this site:/about-site/,Search:/search/;Browse the blog|Locations:/locations/,Posts by date:/year-archive/,Tags:/tags/,Categories:/categories/,Stream:/stream/,Stream archive:/stream/archive/;More|Communications archive:/communications/,The New Word Project:/dictionary/,My story:/testimony/,Locus of Transformation:/transformation-support/,Email list:/email-signup/,Design services:/design/" | split: ";" %}

<div class="row row-cols-1 row-cols-md-3 g-4 mb-4">
  {%- for g in groups -%}
  {%- assign parts = g | split: "|" -%}
  <section class="col">
    <h2 class="h5 fw-bold">{{ parts[0] }}</h2>
    <ul class="list-unstyled mb-0">
      {%- assign links = parts[1] | split: "," -%}
      {%- for l in links -%}{%- assign lp = l | split: ":" %}
      <li><a href="{{ lp[1] | relative_url }}">{{ lp[0] }}</a></li>
      {%- endfor %}
    </ul>
  </section>
  {%- endfor %}
</div>

## Resources

<div class="row row-cols-1 row-cols-md-3 g-4 mb-4">
  <section class="col">
    <h3 class="h6 fw-bold"><a href="{{ '/resources/essays/' | relative_url }}">Academic Essays</a> <span class="text-body-secondary fw-normal">{{ essays.size }}</span></h3>
    <ul class="small">{% for r in essays %}<li><a href="{{ r.url | relative_url }}">{{ r.title | escape }}</a></li>{% endfor %}</ul>
  </section>
  <section class="col">
    <h3 class="h6 fw-bold"><a href="{{ '/resources/articles/' | relative_url }}">Articles</a> <span class="text-body-secondary fw-normal">{{ articles.size }}</span></h3>
    <ul class="small">{% for r in articles %}<li><a href="{{ r.url | relative_url }}">{{ r.title | escape }}</a></li>{% endfor %}</ul>
  </section>
  <section class="col">
    <h3 class="h6 fw-bold"><a href="{{ '/resources/#informational' | relative_url }}">Informational</a> <span class="text-body-secondary fw-normal">{{ informationals.size }}</span></h3>
    <ul class="small">{% for r in informationals %}<li><a href="{{ r.url | relative_url }}">{{ r.title | escape }}</a></li>{% endfor %}</ul>
  </section>
</div>

## Blog Posts

{%- assign by_year = site.posts | group_by_exp: "p", "p.date | date: '%Y'" %}
<div class="row row-cols-1 row-cols-md-2 g-4">
  {%- for g in by_year %}
  <section class="col">
    <h3 class="h6 fw-bold"><a href="{{ '/year-archive/' | relative_url }}#y-{{ g.name }}">{{ g.name }}</a> <span class="text-body-secondary fw-normal">{{ g.size }}</span></h3>
    <ul class="small">{% for p in g.items %}<li><a href="{{ p.url | relative_url }}">{{ p.title | escape }}</a></li>{% endfor %}</ul>
  </section>
  {%- endfor %}
</div>
