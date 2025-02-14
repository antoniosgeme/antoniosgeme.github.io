---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

[**Download PDF Version of CV**]( /assets/CV/CV_AntoniosG.pdf){: .btn}


<div class="publications-list">
  <h2>Journal Articles</h2>
  <ol>
    {% assign journalPublications = site.data.publications | where: 'type', 'journal' | sort: 'year' | reverse %}
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
                {% if lastName == "Gementzopoulos" %}
                  <strong>{{ lastName }} {{ firstInitial }}.</strong>
                {% else %}
                  {{ lastName }} {{ firstInitial }}.
                {% endif %}
              {% else %}
                {% if lastName == "Gementzopoulos" %}
                  <strong>{{ lastName }} {{ firstInitial }}.</strong>,
                {% else %}
                  {{ lastName }} {{ firstInitial }}.,
                {% endif %}
              {% endif %}
            {% else %}
              {% if lastName == "Gementzopoulos" %}
                <strong>{{ lastName }}.</strong>,
              {% else %}
                {{ author }},{% endif %}
            {% endif %}
          {% endfor %}
          ({% if publication.year %}{{ publication.year }}{% endif %})
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
          {% if publication.doi %}
            <a href="https://doi.org/{{ publication.doi }}" target="_blank">DOI: {{ publication.doi | remove: ' ' }}</a>
          {% endif %}
        </p>
      </li>
    {% endfor %}
  </ol>

  <h2>Conference Articles</h2>
  <ol>
    {% assign conferencePublications = site.data.publications | where: 'type', 'conference' | sort: 'year' | reverse %}
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
                {% if lastName == "Gementzopoulos" %}
                  <strong>{{ lastName }} {{ firstInitial }}.</strong>
                {% else %}
                  {{ lastName }} {{ firstInitial }}.
                {% endif %}
              {% else %}
                {% if lastName == "Gementzopoulos" %}
                  <strong>{{ lastName }} {{ firstInitial }}.</strong>,
                {% else %}
                  {{ lastName }} {{ firstInitial }}.,
                {% endif %}
              {% endif %}
            {% else %}
              {% if lastName == "Gementzopoulos" %}
                <strong>{{ lastName }}.</strong>,
              {% else %}
                {{ author }},{% endif %}
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
          {% if publication.doi %}
            <a href="https://doi.org/{{ publication.doi }}" target="_blank">DOI: {{ publication.doi | remove: ' ' }}</a>
          {% endif %}
        </p>
      </li>
    {% endfor %}
  </ol>

  <h2>Conference Abstracts</h2>
  <ol>
   {% assign abstractPublications = site.data.publications | where: 'type', 'abstract' | sort: 'year' | reverse %}
    {% for publication in abstractPublications %}
      <li>
        <p>
          {% assign authors = publication.author | split: ' and ' %}
          {% for author in authors %}
            {% assign authorNames = author | split: ', ' %}
            {% if authorNames.size > 1 %}
              {% assign lastName = authorNames[0] %}
              {% assign firstInitial = authorNames[1] | slice: 0 %}
              {% if forloop.last %}
                {% if lastName == "Gementzopoulos" %}
                  <strong>{{ lastName }} {{ firstInitial }}.</strong>
                {% else %}
                  {{ lastName }} {{ firstInitial }}.
                {% endif %}
              {% else %}
                {% if lastName == "Gementzopoulos" %}
                  <strong>{{ lastName }} {{ firstInitial }}.</strong>,
                {% else %}
                  {{ lastName }} {{ firstInitial }}.,
                {% endif %}
              {% endif %}
            {% else %}
              {% if lastName == "Gementzopoulos" %}
                <strong>{{ lastName }}.</strong>,
              {% else %}
                {{ author }},{% endif %}
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
          {% if publication.doi %}
            <a href="https://doi.org/{{ publication.doi }}" target="_blank">DOI: {{ publication.doi | remove: ' ' }}</a>
          {% endif %}
        </p>
      </li>
    {% endfor %}
  </ol>
</div>
