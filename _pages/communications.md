---
title: Communications Archive
layout: categories-communication
permalink: /communications/
author_profile: true
---

I have started to track the various emails that I send out to groups. A listing of the various communications with each class is below:
 
{% assign items_grouped = site.communications | group_by: 'group' %}
{% for group in items_grouped %}
<h2>{{group.name}}</h2>
<ul>
{% for item in group.items %}
<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
{% endfor %}