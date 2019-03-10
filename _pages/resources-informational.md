---
title: Informational Resources
layout: single
permalink: /resources/
sidebar:
    nav: "resources"
---

I have written a number of different posts from various notes I took during my studies, or presentations I have given that that can be viewed. They are on a number of different topics, mostly focused on social work. The following is a list of all of the informational posts in my resources.

{% assign informationals = site.resources | where: "categories", "Informational" %}

<ul>
{% for resource in informationals %}
<li>
    <a href="{{ resource.url }}">{{ resource.title }}</a>
</li>  
{% endfor %}
</ul>


I have written a number of different articles that that can be viewed. They are on a number of different topics, mostly focused on social work. The following is a list of all of the articles in my resources.

{% assign articles = site.resources | where: "categories", "Article" %}

<ul>
{% for resource in articles %}
<li>
    <a href="{{ resource.url }}">{{ resource.title }}</a>
</li>  
{% endfor %}
</ul>