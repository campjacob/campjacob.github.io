---
title: Playground
permalink: /play
layout: single
tags:
    - L- Tag 2
---
I'm a page with tags.

{% assign starter-0 = '{{ {{ page.tag[0] }} | slice: 1 }}' %}
{% if  starter-0 == 'L-' %}
  Location:
{% endif %}






