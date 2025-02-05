---
layout: archive
title: "CV"
permalink: /wholeCV/
author_profile: true
---

[**Download PDF Version of CV**]( /assets/CV/CV_AntoniosG.pdf){: .btn}


## Education
- Ph.D. Aerospace Engineering, University of Maryland, College Park, 2025
- M.Res. Aeronautical Engineering, University of Cambridge, 2019
- B.S. Mechanical Engineering, New York University, 2018

## Research Experience

- **University of Maryland, College Park**  
  *Postdoctoral Associate, Department of Aerospace Engineering (2020–2025)*  
  **Laboratory:** High-Speed Aerodynamics and Propulsion Laboratory (HAPL)  

- **University of Maryland, College Park**    
  *Graduate Research Assistant, Department of Aerospace Engineering (2020–2025)*  
  **Laboratory:** Separated and Transient Aerodynamics Laboratory (STAL)  
  **Thesis:** “Gust encounter flow physics with applications to flow sensing and control”  
  **Advisor:** Dr. Anya Jones

- **NASA Goddard Space Flight Center**  
  *Intern, University Space Research Association (USRA) (2024)*

- **NATO Applied Vehicle Technology (AVT) Panel**  
  *Technical Team Member, AVT–347: Large-amplitude gust mitigation strategies for rigid wings (2021–2024)*

- **Whittle Laboratory, University of Cambridge**  
  *Graduate Research Assistant (2018–2019)*  
  **Thesis:** “Prediction of Low Frequency Thermoacoustic Instabilities”

- **Dynamical Systems Laboratory, New York University (Tandon School of Engineering)**  
  *Undergraduate Researcher (2016–2018)*

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
