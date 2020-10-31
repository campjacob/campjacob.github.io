---
layout: single
title: Micro Posts
permalink: /microposts/
author_profile: "true"
---

I'm not a web designer, even though I like to play one on my website. Lately I've been fascinated with the concept of the [Indie Web](https://indieweb.org/why). I don't want to post everything on my website (e.g. Tweets / photos) prior to them being shared to social media, but I do like the idea of having all of the stuff on my website.

That being said, you can see....


{% assign mposts = site.microposts %}

{% for post in mposts %}

{{ post.content }}
 
{% endfor %}