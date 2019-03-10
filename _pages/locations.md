---
title: Locations
layout: locations
permalink: /locations/
---

<ul class="taxonomy__index">
{% for tag in site.tags %}

{% assign t = tag | where_exp: "item", "item contains 'L--'" | first %}
{% assign posts = tag | last %}

{% for post in posts %}
{% if forloop.first %}
{% if post.tags contains t %}
<li>
    <strong>
        <a href="#{{ t | slugify | downcase }}">{{ t | replace: 'L--', '' }}</a>
    </strong>
    <span class="taxonomy__count"></span>
</li>
{% endif %}
{% endif %}
{% endfor %}
{% endfor %}

</ul>

{% for tag in site.tags %}
{% assign t = tag | where_exp: "item", "item contains 'L--'" | first %}
{% assign posts = tag | last %}
{% for post in posts %}
{% if post.tags contains t %}
{% if forloop.first %}
<section id="{{ t | slugify | downcase }}" class="taxonomy__section">
<h2 class="archive__subtitle">{{ t | replace: 'L--', '<i class="fas fa-map-pin"></i> ' }}</h2>
<div class="entries-{{ page.entries_layout | default: 'list' }}">
<ul>
{% endif %}
<li><a href="{{ post.url }}">{{ post.title }}</a></li>
{% if forloop.last %}
</ul></div>
<a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: 'Back to Top' }} &uarr;</a>
</section>
{% endif %}
{% endif %}
{% endfor %}
{% endfor %}

