---
title: Presentations and Handouts Informational Resources
layout: single
permalink: /resources/presentations-handouts-informationals/
sidebar:
    nav: "resources"
---

{% assign informationals = site.resources | where: "categories", "Informational" %}

There are various resources that can be found that are either presentations I previously completed or handouts that are associated with them. You can see the presentations listed:

{% assign presentations-informationals = informationals | where: "tags", "Presentation" %}
{% for resource in presentations-informationals %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}

You can see the handouts listed:

{% assign handouts-informationals = informationals | where: "tags", "Handout" %}
{% for resource in handouts-informationals %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}