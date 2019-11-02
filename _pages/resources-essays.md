---
title: Academic Essays
layout: single
permalink: /resources/essays/
sidebar:
    nav: "resources"
---

I have written a number of different essays that that can be viewed. They are on a number of different topics, mostly my writing for while I am working on my Ph.D. in Transformative Studies at the California Institute of Integral studies. The following is a list of all of the essays in my resources.

{% assign articles = site.resources | where: "categories", "Essay" %}

<ul>
{% for resource in articles %}
<li>
    <a href="{{ resource.url }}">{{  resource.title  }}</a>
</li>  
{% endfor %}
</ul>