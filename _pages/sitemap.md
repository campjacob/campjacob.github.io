---
title: Sitemap
layout: single
permalink: /sitemap/
author_profile: true
---

<ul>
  <li>Informational Resources</li>
    {% assign informationals = site.resources | where: "categories", "Informational" %}
    <ul>
      {% for resource in informationals %}
      <li><a href="{{ resource.url }}">{{ resource.title }}</a></li>  
      {% endfor %}
    </ul>
    <li>Article Resources</li>
    {% assign articles = site.resources | where: "categories", "Article" %}
    <ul>
    {% for resource in articles %}
      <li><a href="{{ resource.url }}">{{ resource.title }}</a></li>  
    {% endfor %}
    </ul>
    <li>Blog Posts</li>
    <ul>
    {% for post in site.posts %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>  
    {% endfor %}
    </ul>
</ul>
* Other Pages
  - [404 Error](/404.html)
  - [About Site](/about-site/)
  - [Categories](/categories/)
  - [Contact](/contact/)
  - [CV](/cv/)
  - [Design](/design/)
  - [Locations](/locations/)
  - [Resource Articles](/resources/articles/)
  - [Informational Resources](/resources/)
  - [Sitemap](/sitemap/)
  - [Tags](/tags/)
  - [Testimony](/testimony/)
  - [Year Archive](/year-archive/)
  - [Home](/)
