---
layout: single
title: Micro Posts
permalink: /microposts/
author_profile: "true"
---

I'm not a web designer, even though I like to play one on my website. Lately I've been fascinated with the concept of the [Indie Web](https://indieweb.org/why). I really like the idea of owning my own data, and being able to have my website be the place that I have links to everything I'm doing. These microposts are things that I have shared on social media, also added here for your reading pleasure.

{% assign instagram_micropost = site.microposts | where: "categories", "instagram" | reverse %}
{% assign twitter_micropost = site.microposts | where: "categories", "tweet" | reverse %}

<h1><i class="fab fa-instagram"></i> Instagram Posts</h1>
You can find me as [@campjacob](https://www.instagram.com/campjacob/). You can see my latest post, or a list of all my posts. 

{% for last_insta in instagram_micropost limit:1 %}
{{ last_insta.content }}
{% endfor %}

<ul>
{% for ipost in instagram_micropost %}
<li>{{ ipost.date | date_to_string }} <a href="{{ ipost.url }}">{{ ipost.post_text }}</a> (<a href="{{ ipost.post_url }}">Original</a>)</li>
{% endfor %}
</ul>

<h1><i class="fab fa-twitter"></i> Twitter Posts</h1>
You can find me as [@campjacob](https://twitter.com/campjacob). You can see my latest post, or a list of all my posts. 

{% for last_tweet in twitter_micropost limit:1 %}
{{ last_tweet.content }}
{% endfor %}


<ul>
{% for tpost in twitter_micropost %}
<li>{{ tpost.date | date_to_string }} <a href="{{ tpost.url }}">{{ tpost.post_text }}</a> (<a href="{{ tpost.post_url }}">Original</a>)</li>
{% endfor %}
</ul>