---
layout: page
navigation_title: About
title: About Data + Donuts
permalink: /about/

---

<p>Data + Donuts is a morning speaker series and networking event that brings together the makers and doers that are changing local government from the ground up by harnessing technology and data to drive meaningful change.  It is a joint, collaborative effort between the County of Los Angeles, the City of Los Angeles, and the local L.A. civic technology community.</p>

<p>Our speakers and networking sessions will delve into the latest topics in technology: Big Data, Platform as a Service, DevOps, Open Data, Analytics and Visualization, Community Engagement, Civic Technology and more.</p>

<img src="{{site.baseurl}}/images/digital-summit-award.jpg">
<caption><em>Data + Donuts organizers receiving 2018 Digital Government Summit Award</em></caption>

<br />

<h1 id="covid">Covid Policy 2023</h1>

<p>As the pandemic continues and changes, Data + Donuts re-enters live events with a set of Covid protocols that seeks to create an event environment that promotes equity, access and public health as a communal vision. While we duly hold that no event has the ability to be completely safe, our hope is that these protocols create a safer environment for more participants.</p>

<p>Moving forward, Data + Donuts will **require masks for all attendees**. It is important to note that while masking is not required at LACI, our specific event does require masks. We ask that you come prepared with your PPE and if needed we can provide masks on location when checking in. We will continue to monitor COVID data as the event nears and should they represent an unsafe event environment we will notify attendees promptly. Thank you for committing to this shared vision and if there’s any other ways we can more inclusively create this event please let us know. </p>

<h1>Past Speakers</h1>
<ul>
{% for speaker in site.data.speakers %}
  <li>
      <strong>{{ speaker[0] }}</strong>, {{ speaker[1].title }}, {{ speaker[1].org }}
  </li>
{% endfor %}
</ul>
