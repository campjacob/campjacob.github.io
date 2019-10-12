---
title: Directions Program Evaluation Informational Resources
layout: single
permalink: /resources/directions-program-evalaution-informationals/
sidebar:
    nav: "resources"
---

{% assign informationals = site.resources | where: "categories", "Informational" %}
{% assign articles = site.resources | where: "categories", "Article" %}

My Master's Degree Terminal Project was an in-depth program evaluation. There are a number of resources related to it, if you are interested in seeing how a program evaluation can be put together. The [Overview of The Crisis Residential Center’s Directions Program Evaluation: For the 2006-2008 Financial Grant Years Study](/resources/overview-of-the-crisis-residential-centers-directions-program-evaluation) is a good place to start and includes a great broad perspective of the entire project. You can also see a list of all of the articles and informational resources below:

{% assign directions-program-informationals = informationals | where: "tags", "Directions Program Evaluation" %}
{% for resource in directions-program-informationals %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}

As well, you can see the actual final articles about the program evaluation as well.

{% assign directions-program-articles = articles | where: "tags", "Directions Program Evaluation" %}
{% for resource in directions-program-articles %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}
