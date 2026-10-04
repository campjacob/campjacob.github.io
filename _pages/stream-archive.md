---
title: Stream Archive
layout: foundation
nav_group: stream
author_sidebar: true
permalink: /stream/archive/
redirect_from:
  - /microposts/archive/
---
{%- comment -%} Legacy tweets from the _microposts collection. Instagram and TikTok posts now come in through scripts/import-stream.py and show on /stream/. {%- endcomment -%}
{%- assign legacy_kinds = "tweet" | split: "," -%}
{%- assign legacy = "" | split: "" -%}
{%- for p in site.microposts -%}{%- assign k = p.categories | first -%}{%- if legacy_kinds contains k -%}{%- assign legacy = legacy | push: p -%}{%- endif -%}{%- endfor -%}
{%- assign legacy = legacy | sort: "date" | reverse -%}
{%- assign by_year = legacy | group_by_exp: "p", "p.date | date: '%Y'" -%}

<article class="stream-archive">

<header class="my-4">
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb small mb-2">
      <li class="breadcrumb-item"><a href="/stream/">Stream</a></li>
      <li class="breadcrumb-item active" aria-current="page">Archive</li>
    </ol>
  </nav>
  <h1 class="fw-bolder">Stream Archive</h1>
  <p class="lead mb-1">Posts I shared on Twitter between 2019 and 2022, before I moved to the fediverse. They are kept here as a record. My Instagram photos and TikTok videos are in the <a href="/stream/">stream</a>.</p>
  <p class="text-body-secondary small mb-0"><i class="fas fa-archive" aria-hidden="true"></i> {{ legacy | size }} posts. Links to the originals may no longer work.</p>
</header>

{%- for year in by_year -%}
<section class="my-4">
  <h2 class="h5 fw-bold border-bottom pb-1">{{ year.name }} <span class="fw-normal text-body-secondary small">({{ year.items | size }})</span></h2>
  <ul class="list-unstyled mb-0">
    {%- for p in year.items -%}
    {%- assign kind = p.categories | first | default: p.categories -%}
    {%- case kind -%}
      {%- when "tweet" -%}{%- assign icon = "fab fa-twitter" -%}{%- assign label = "Twitter" -%}
      {%- when "instagram" -%}{%- assign icon = "fab fa-instagram" -%}{%- assign label = "Instagram" -%}
      {%- when "tiktok" -%}{%- assign icon = "fab fa-tiktok" -%}{%- assign label = "TikTok" -%}
      {%- else -%}{%- assign icon = "fas fa-comment" -%}{%- assign label = "Post" -%}
    {%- endcase -%}
    <li class="d-flex gap-3 py-2 border-bottom border-light-subtle">
      <i class="{{ icon }} fa-fw mt-1 text-body-secondary" title="{{ label }}" aria-label="{{ label }}"></i>
      <div class="flex-grow-1">
        <a href="{{ p.url | relative_url }}" class="text-decoration-none text-body">{{ p.post_text | default: p.title | strip_html | truncate: 220 }}</a>
        <div class="small text-body-secondary mt-1">
          {{ p.date | date: "%b %-d, %Y" }}
          {%- if p.post_url %} &middot; <a href="{{ p.post_url }}" class="text-body-secondary" rel="noopener">Original on {{ label }}</a>{% endif %}
        </div>
      </div>
    </li>
    {%- endfor -%}
  </ul>
</section>
{%- endfor -%}

</article>
