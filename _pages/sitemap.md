---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A comprehensive overview of all content on this academic website. For search engines, an [XML version]({{ base_path }}/sitemap.xml) is available.

<h2>Main Pages</h2>
{% for post in site.pages %}
  {% unless post.sitemap == false %}
    {% include archive-single.html %}
  {% endunless %}
{% endfor %}

<h2>Posts</h2>
{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}

{% capture written_label %}'None'{% endcapture %}

{% for collection in site.collections %}
{% unless collection.output == false or collection.label == "posts" %}
  {% capture label %}{{ collection.label }}{% endcapture %}
  {% if label != written_label %}
  <h2>{{ label }}</h2>
  {% capture written_label %}{{ label }}{% endcapture %}
  {% endif %}
{% endunless %}
{% for post in collection.docs %}
  {% unless collection.output == false or collection.label == "posts" or post.sitemap == false %}
  {% include archive-single.html %}
  {% endunless %}
{% endfor %}
{% endfor %}
