---
layout: page
navigation_title: About
title: About Data + Donuts
permalink: /about/

---

<p>Data + Donuts is a morning speaker series and networking event that brings together the makers and doers that are changing local government from the ground up by harnessing technology and data to drive meaningful change.  It is a joint, collaborative effort between the County of Los Angeles, the City of Los Angeles, and the local L.A. civic technology community.</p>

<p>Our speakers and networking sessions will delve into the latest topics in technology: Big Data, Platform as a Service, DevOps, Open Data, Analytics and Visualization, Community Engagement, Civic Technology and more.</p>

<p>Doors Open @ 8am<br />
Speaker Begins @ 9am<br /> 
Doors Close @ 10am</p>

<h1>Past Speakers</h1>>
<ul>
{% for member in site.data.organisers %}
  <li>
<!--     <a href="https://github.com/{{ member.github }}">
 -->      {{ organiser.name }}
    </a>
  </li>
{% endfor %}
</ul>

<p></p>