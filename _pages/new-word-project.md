---
permalink: /new-word-project/
title: The New Word Project
date: 2019-09-03
classes: wide
layout: single
author_profile: true
---

This project is just a little bit of fun for me. You can see [The of the Blog Post](#) for information about how I made it, where the content of the definitions came from, and all of that information. This page is a compilation of all of the words in the New Word Project. Join me in my journey as I discover new words.

<section class="term">

{% for term in site.dictionary %}
<div class="term-entry-list">
    <div class="card" style="float: left;">
        <div class="card-header">
            {% if term.dictionary-picture %}
            <img src="/assets/media/{{ dictionary-picture-file }}" alt="word" style="background-size: cover;">
            {% endif %}
        </div>
        <div class="card-text">
        {{ term.content }}
        <p>See dictionary entry for <a href="/dictionary/{{ term.title }}" class="btn btn--primary">{{ term.title }}</a></p>
        </div>
    </div>
</div>

{% endfor %}

</section>