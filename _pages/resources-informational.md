---
title: Informational Resources
layout: single
permalink: /resources/
toc: true
toc_label: "Table of Contents"
sidebar:
    nav: "resources"
---

I've compiled a number of different resources over the years. Much of it is academic writing or notes that I took either while I was studying for my Bachelors in Social Work (BASW) and my Masters in Social Work (MSW) while I was studying at Eastern Washington University back in 2007-2009. I'm also including a number of essays and other resources from working on Ph.D. in Transformative Studies at the California Institute of Integral Studies that I started in 2019. This page should include links to all of those resources. Make sure to check out my [blog](/blog/) for more of my non academic writing. Although there are some presentations that I gave earlier on in my career, more of my talks and presentations that I give while teaching or at other events are posted in the [presentation](https://presentations.jacobrcampbell.com) section of my website.

## Academic Essays

I have written a number of different essays that that can be viewed. They are on a number of different topics, mostly my writing for while I am working on my Ph.D. in Transformative Studies at the California Institute of Integral studies. The following is a list of all of the essays in my resources.

{% assign essays = site.resources | where: "categories", "Essay" %}
{% for resource in essays %}
- [{{  resource.title  }}]({{ resource.url }})
{% endfor %}

## Academic Articles

There are number of academically focused articles that I have posted on my website. They are on a number of different topics, mostly focused on social work. The following is a list of all of the articles in my resources.

{% assign articles = site.resources | where: "categories", "Article" %}
{% for resource in articles %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}

## Informational Resources

I have written a number of different posts from various notes I took during my studies, or presentations I have given that that can be viewed. They are on a number of different topics, mostly focused on social work. They include research methods informational resources, the direction program evaluation, presentations and handouts, and other informational resources.

### Research Methods Informational Resources

Research methods is a difficult subject for a number of students and practitioners. It can be scary to dive into for some, and it's topics can be challenging. My post, [Research Methods & Evidence Based Practice](/resources/research-methods-evidence-based-practice), gives a good overview of research and many of the article included. The following would a list of the various resources that pertain to research methods.

{% assign informationals = site.resources | where: "categories", "Informational" %}

{% assign research-methods-informationals = informationals | where: "tags", "Research Methods" %}
{% for resource in research-methods-informationals %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}

### Directions Program Evaluation Informational Resources

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

### Presentations And Handouts Informational Resources

There are various resources that can be found that are either presentations I previously completed or handouts that are associated with them. You can see the presentations listed:

{% assign presentations-informationals = informationals | where: "tags", "Presentation" %}
{% for resource in presentations-informationals %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}

You can see the handouts listed:

{% assign handouts-informationals = informationals | where: "tags", "Handout" %}
{% for resource in handouts-informationals %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}

### Other Informational Resources

There are also a couple other informational posts that don't necessarily fit anywhere else. They are as follows:

{% assign other-informationals = informationals | where: "tags", "Other" %}
{% for resource in other-informationals %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}

