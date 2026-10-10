---
title: Articles
layout: foundation
nav_group: resources
author_sidebar: true
permalink: /resources/articles/
---
{%- assign articles = "" | split: "" -%}
{%- for r in site.resources -%}{%- if r.path contains "/articles/" -%}{%- assign articles = articles | push: r -%}{%- endif -%}{%- endfor -%}
{%- assign articles = articles | sort: "date" | reverse -%}

<article class="resources-list">

<header class="my-4">
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb small mb-2">
      <li class="breadcrumb-item"><a href="/resources/">Resources</a></li>
      <li class="breadcrumb-item active" aria-current="page">Articles</li>
    </ol>
  </nav>
  <h1 class="fw-bolder">Articles</h1>
  <p class="lead mb-1">Academically focused papers and reports, mostly on social work practice and research. Most have a downloadable PDF version.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-file-alt" aria-hidden="true"></i> {{ articles | size }} articles, newest first.</p>
</header>

<div class="card shadow-sm my-4">
  <ul class="list-group list-group-flush">
    {%- for r in articles -%}
    {% include resource-list-item.htm resource=r %}
    {%- endfor -%}
  </ul>
</div>

</article>
