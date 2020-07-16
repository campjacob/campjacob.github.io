---
layout: single
title: Micro Posts
permalink: /microposts/
author_profile: "true"
---

I'm not a web designer, even though I like to play one on my website. Lately I've been fascinated with the concept of the [Indie Web](https://indieweb.org/why). I don't want to post everything on my website (e.g. Tweets / photos) prior to them being shared to social media, but I do like the idea of having all of the stuff on my website.

That being said, you can see....




{% assign posts = paginator.posts | concat: site.microposts | sort: "date" %} 
{% for post in posts %}
  {% if post.collection == 'posts' %}
    <h2>{{ post.title }}</h2>
    <div>{{ post.content }}</div>
  {% elsif post.collection == 'tweets' %}
    {% comment %} If I am not mistaken, twitter have no title concept {% endcomment %}
    <h2>There was a bird singing about:</h2> 
    <div>{{ post.content }}</div>
  {% elsif post.collection == 'instagram' %}
    {% comment %} So, now, it can fit any social media of your choice {% endcomment %}
  {% endif %}
{% endfor %}
