---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<div class="publications-list">
  <h2>Journal Articles</h2>
  <ul>
    {% for publication in site.data.publications %}
      {% if publication.type == 'journal' %}
        <li>
          <p>
            {% assign authors = publication.author | split: ' and ' %}
            {% for author in authors %}
              {% if forloop.last %}
                {% if authors.size > 1 %}
                  and {{ author | split: ', ' | reverse | join: ' ' }}
                {% else %}
                  {{ author | split: ', ' | reverse | join: ' ' }}
                {% endif %}
              {% else %}
                {{ author | split: ', ' | reverse | join: ' ' }},
              {% endif %}
            {% endfor %}
            ({% if publication.year %}{{ publication.year }}.{% endif %})
            {% if publication.title %}
              {% if publication.year %}. {% endif %}
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
      {% endif %}
    {% endfor %}
  </ul>
  
  <h2>Conference Articles</h2>
  <ul>
    {% for publication in site.data.publications %}
      {% if publication.type == 'conference' %}
        <li>
          <p>
            {% assign authors = publication.author | split: ' and ' %}
            {% for author in authors %}
              {% if forloop.last %}
                {% if authors.size > 1 %}
                  and {{ author | split: ', ' | reverse | join: ' ' }}
                {% else %}
                  {{ author | split: ', ' | reverse | join: ' ' }}
                {% endif %}
              {% else %}
                {{ author | split: ', ' | reverse | join: ' ' }},
              {% endif %}
            {% endfor %}
            ({% if publication.year %}{{ publication.year }}.{% endif %})
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
      {% endif %}
    {% endfor %}
  </ul>
</div>
