---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

[**Download PDF Version of CV**]( /assets/CV/CV_AntoniosG.pdf){: .btn}

A complete and current list is also available on [Google Scholar]({{ site.author.googlescholar }}).

<div class="publications-list">

  {% assign journalPublications = site.data.publications | where: 'type', 'journal' | sort: 'year' | reverse %}

  {%- comment -%}
    Detect whether any journal entry is flagged as under-review / in-prep / submitted
    (we look at the `journal` field for keywords). If so, render a separate section.
  {%- endcomment -%}
  {% assign hasUnderReview = false %}
  {% for p in journalPublications %}
    {% assign j = p.journal | default: "" | downcase %}
    {% if j contains "under review" or j contains "in preparation" or j contains "submitted" %}
      {% assign hasUnderReview = true %}
    {% endif %}
  {% endfor %}

  <h2>Journal Articles</h2>
  <ol class="pub-list">
    {% for publication in journalPublications %}
      {% assign j = publication.journal | default: "" | downcase %}
      {% unless j contains "under review" or j contains "in preparation" or j contains "submitted" %}
        {% include publication-entry.html publication=publication kind="journal" %}
      {% endunless %}
    {% endfor %}
  </ol>

  {% if hasUnderReview %}
    <h2>Under Review &amp; In Preparation</h2>
    <ol class="pub-list">
      {% for publication in journalPublications %}
        {% assign j = publication.journal | default: "" | downcase %}
        {% if j contains "under review" or j contains "in preparation" or j contains "submitted" %}
          {% include publication-entry.html publication=publication kind="journal" %}
        {% endif %}
      {% endfor %}
    </ol>
  {% endif %}

  <h2>Conference Articles</h2>
  <ol class="pub-list">
    {% assign conferencePublications = site.data.publications | where: 'type', 'conference' | sort: 'year' | reverse %}
    {% for publication in conferencePublications %}
      {% include publication-entry.html publication=publication kind="conference" %}
    {% endfor %}
  </ol>

  <h2>Conference Abstracts</h2>
  <ol class="pub-list">
    {% assign abstractPublications = site.data.publications | where: 'type', 'abstract' | sort: 'year' | reverse %}
    {% for publication in abstractPublications %}
      {% include publication-entry.html publication=publication kind="abstract" %}
    {% endfor %}
  </ol>

</div>

<style>
.publications-list h2{
  margin-top:28px;color:#2c3e50;border-bottom:2px solid #3498db;
  padding-bottom:6px;display:inline-block
}
.pub-list{padding-left:22px}
.pub-entry{
  padding:10px 0;border-bottom:1px solid #f1f3f5;
  display:flex;flex-wrap:wrap;gap:8px;align-items:baseline;justify-content:space-between
}
.pub-entry:last-child{border-bottom:none}
.pub-cite{flex:1 1 70%;line-height:1.5;color:#3a4754}
.pub-cite em{color:#2c3e50}
.pub-links{flex:0 0 auto;display:flex;gap:6px;flex-wrap:wrap}
.paper-link{
  display:inline-block;padding:3px 12px;background:#3498db;color:#fff !important;
  border-radius:999px;font-size:.82rem;text-decoration:none;white-space:nowrap
}
.paper-link:hover{background:#217dbb}
.paper-link--preprint{background:#7f8c8d}
.paper-link--preprint:hover{background:#5d6d6e}
@media (max-width:600px){
  .pub-entry{flex-direction:column;align-items:flex-start}
}
</style>
