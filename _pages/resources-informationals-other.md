---
title: Other Informational Resources
layout: single
permalink: /resources/other-informationals/
sidebar:
    nav: "resources"
---

{% assign informationals = site.resources | where: "categories", "Informational" %}

There are also a couple other informational posts that don't necessarily fit anywhere else. They are as follows:

{% assign other-informationals = informationals | where: "tags", "Other" %}
{% for resource in other-informationals %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}
