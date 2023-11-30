---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


<div class="publications-list">
  <h2>Publications</h2>
  <ul>
    {% for publication in site.data.publications %}
      <li>
        <h3>{{ publication.title }}</h3>
        <p><strong>Authors:</strong> {{ publication.author }}</p>
        <p><strong>Journal:</strong> {{ publication.journal }}</p>
        <p><strong>Volume:</strong> {{ publication.volume }}</p>
        <p><strong>Pages:</strong> {{ publication.pages }}</p>
        <p><strong>Year:</strong> {{ publication.year }}</p>
        <p><strong>Publisher:</strong> {{ publication.publisher }}</p>
      </li>
    {% endfor %}
  </ul>
</div>

