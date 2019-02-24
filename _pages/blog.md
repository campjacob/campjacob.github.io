---
layout: home
pagination: 
  enabled: true
  category: Personal Blog
title:  "Snapshots: My Blog"
permalink: "/blog/"
author_profile: "true"
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: "assets/media/brazil-boat-sunset-blog-header.jpg"
  caption: "Photo credit: A photo I took during my [**Jaunt Down South**](http://fixme.com) while on the Amazon in Brazil."
excerpt: "Little bits and pieces of my life written down and shared with you."
---

{% for post in site.posts %}
       
<h1><a href="{{ post.url }}">{{ post.title }}</a></h1>
<p>Posted on <a href="{{ post.url }}">{{ post.date | date: "%A %B %-d, %Y" }}</a> by <a href="/contact">Jacob Campbell</a>.</p>

{{ post.content }}


{% endfor %}
