---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<div class="publications-list">
  <h2>Publications</h2>
  <ol>
    {% for publication in site.data.publications %}
      <li>
        <h3>{{ publication.title }}</h3>
        <p><strong>Authors:</strong> {{ publication.author }}</p>
        <p><strong>Journal/Book Title:</strong> {{ publication.journal | default: publication.booktitle }}</p>
        <p><strong>Volume/Number:</strong> {{ publication.volume | default: publication.number }}</p>
        <p><strong>Pages:</strong> {{ publication.pages }}</p>
        <p><strong>Year:</strong> {{ publication.year }}</p>
        <p><strong>Publisher:</strong> {{ publication.publisher | default: "N/A" }}</p>
      </li>
    {% endfor %}
  </ol>
</div>
