---
title: Article Resources
layout: single
permalink: /resources/articles/
sidebar:
    nav: "resources"
---

I have written a number of different articles that that can be viewed. They are on a number of different topics, mostly focused on social work. The following is a list of all of the articles in my resources.

{% assign articles = site.resources | where: "categories", "Article" %}

<ul>
{% for resource in articles %}
<li>
    <a href="{{ resource.url }}">{{ resource.title }}</a>
</li>  
{% endfor %}
</ul>