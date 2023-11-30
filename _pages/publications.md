---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<div class="publications-list">
  <h2>Journal Articles</h2>
  <ol>
    {% assign journalPublications = site.data.publications | where: 'type', 'journal' %}
    {% for publication in journalPublications %}
      <li>
        <p>
          {% assign authors = publication.author | split: ' and ' %}
          {% for author in authors %}
            {% assign authorNames = author | split: ', ' %}
            {% if authorNames.size > 1 %}
              {% assign lastName = authorNames[0] %}
              {% assign firstInitial = authorNames[1] | slice: 0 %}
              {% if forloop.last %}
                and {{ lastName }} {{ firstInitial }}.
              {% else %}
                {{ lastName }} {{ firstInitial }}.,
              {% endif %}
            {% else %}
              {{ author }},
            {% endif %}
          {% endfor %}
          ({% if publication.year %}{{ publication.year }}{% endif %})
          {% if publication.title %}
            {% if publication.year %} {% endif %}
            <strong>{{ publication.title }}</strong>.
          {% endif %}
          {% if publication.journal %}
            {{ publication.journal }},
          {% endif %}
          {% if publication.volume %}
            {{ publication.volume }},
          {% endif %}
          {% if publication.pages %}
            {{ publication.pages }}
          {% endif %}
        </p>
      </li>
    {% endfor %}
  </ol>
  
  <h2>Conference Articles</h2>
  <ol>
    {% assign conferencePublications = site.data.publications | where: 'type', 'conference' %}
    {% for publication in conferencePublications %}
      <li>
        <p>
          {% assign authors = publication.author | split: ' and ' %}
          {% for author in authors %}
            {% assign authorNames = author | split: ', ' %}
            {% if authorNames.size > 1 %}
              {% assign lastName = authorNames[0] %}
              {% assign firstInitial = authorNames[1] | slice: 0 %}
              {% if forloop.last %}
                and {{ lastName }} {{ firstInitial }}.
              {% else %}
                {{ lastName }} {{ firstInitial }}.,
              {% endif %}
            {% else %}
              {{ author }},
            {% endif %}
          {% endfor %}
          ({% if publication.year %}{{ publication.year }}{% endif %})
          {% if publication.title %}
            {% if publication.year %}. {% endif %}
            <strong>{{ publication.title }}</strong>.
          {% endif %}
          {% if publication.booktitle %}
            {{ publication.booktitle }},
          {% endif %}
          {% if publication.pages %}
            {{ publication.pages }}
          {% endif %}
        </p>
      </li>
    {% endfor %}
  </ol>
</div>
