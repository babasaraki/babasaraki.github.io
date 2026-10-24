---
layout: page
permalink: /research/
title: Research
eyebrow: Programme
lead: >-
  Four strands, one question running through them — how do you turn sequence
  data into a decision somebody can act on?
---
<div class="grid grid-2">
{% for r in site.data.research %}
  <article class="card">
    <div class="card-icon">{% include icon.html name=r.icon %}</div>
    <h3>{{ r.title }}</h3>
    <p class="small muted">{{ r.summary }}</p>
    <ul>{% for pt in r.points %}<li>{{ pt }}</li>{% endfor %}</ul>
  </article>
{% endfor %}
</div>

<h2 style="margin-top:2.5rem">Software and resources</h2>
<div class="grid grid-2">
{% for sw in site.data.software %}
  <article class="card">
    <div class="card-icon">{% include icon.html name=sw.icon %}</div>
    <h3 style="font-size:1.05rem">
      {% if sw.url %}<a href="{{ sw.url }}" target="_blank" rel="noopener">{{ sw.name }}</a>{% else %}{{ sw.name }}{% endif %}
    </h3>
    <div class="meta"><span class="tag">{{ sw.kind }}</span>{% if sw.repo %}<span class="tiny">{{ sw.repo }}</span>{% endif %}</div>
    {% if sw.summary and sw.summary != "" %}<p class="small muted" style="margin:.6rem 0 0">{{ sw.summary }}</p>{% endif %}
  </article>
{% endfor %}
</div>

<h2 style="margin-top:2.5rem">Interests</h2>
<ul class="pill-list">
  {% for i in site.data.profile.interests %}<li class="chip">{{ i }}</li>{% endfor %}
</ul>

<h2 style="margin-top:2.5rem">Methods and tools</h2>
<div class="grid grid-3">
  {% for g in site.data.profile.skills %}
    <div class="card">
      <h3 style="font-size:1rem">{{ g.group }}</h3>
      <ul>{% for s in g.items %}<li>{{ s }}</li>{% endfor %}</ul>
    </div>
  {% endfor %}
</div>

<div class="callout" style="margin-top:2.5rem">
  <strong>Students and collaborators.</strong>
  I supervise undergraduate and postgraduate projects in genomics and bioinformatics, and I am glad
  to hear from people who want to work on any of the strands above.
  <a href="{{ '/contact/' | relative_url }}">Write to me</a>.
</div>
