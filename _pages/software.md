---
layout: archive
title: "Code"
permalink: /code/
author_profile: true
---

<p class="software-lede">
This page collects code projects that I use for research, teaching, and computational exploration.
</p>

## Projects

{% assign software_items = site.data.software | default: empty %}
{% if software_items.size > 0 %}
  <div class="software-grid">
    {% for item in software_items %}
      <section class="software-card">
        <h2>{{ item.title }}</h2>
        {% if item.description %}
          <p>{{ item.description }}</p>
        {% endif %}
        {% if item.topics %}
          <p class="software-card__topics">
            {% for topic in item.topics %}
              <span>{{ topic }}</span>
            {% endfor %}
          </p>
        {% endif %}
        <p class="software-card__links">
          {% if item.repo_url %}
            <a class="btn btn--primary" href="{{ item.repo_url }}">Repository</a>
          {% endif %}
        </p>
      </section>
    {% endfor %}
  </div>
{% else %}
  <section class="software-card">
    <h2>GitHub repositories</h2>
    <p>
      Add repositories to <code>_data/software.yml</code> and they will appear here automatically.
    </p>
    <p class="software-card__links">
      <a class="btn btn--primary" href="https://github.com/{{ site.author.github }}">View GitHub profile</a>
    </p>
  </section>
{% endif %}

<style>
.software-lede{
  font-size:1.05rem;line-height:1.6;color:#34495e;
  background:#fff;border:1px solid #e1e5e9;border-left:4px solid #1f7a8c;
  border-radius:12px;padding:20px 24px;margin:24px 0
}
.software-grid{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin:24px 0
}
.software-card{
  background:#fff;border:1px solid #e1e5e9;border-left:4px solid #2c3e50;
  border-radius:12px;padding:22px
}
.software-card h2{margin-top:0;color:#2c3e50}
.software-card__tagline{margin-top:0;color:#1f7a8c}
.software-card p{line-height:1.6;color:#3a4754}
.software-card__topics{margin:14px 0}
.software-card__topics span{
  display:inline-block;margin:0 8px 8px 0;padding:4px 10px;border-radius:999px;
  background:#eef6f8;color:#1f5260;font-size:.9rem
}
.software-card__links{margin:18px 0 0}
</style>