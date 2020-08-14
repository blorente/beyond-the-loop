---
layout: page
title: Recurring Series
subtitle: Some of the series of this blog
call_to_action: ["Like any of these series?", "Get notified whenever new content is up!"]
---

Here are some series that I'll keep posting:

**Programming Fundamentals**: Programming is primarily a thought process. Learning how to think the right way about it, how to ask the right questions and find out the right answers is the quickest way to get exponentially better. These topics are timeless, and vital for your development as a programmer. [See All](../tags/#Programming%20Fundamentals)

<div class="posts-list"><ul>
  {% for tag in site.tags %}{% if tag[0] == "Programming Fundamentals" %}{% assign posts = tag[1] | slice:0, 3 %}{% for post in posts %}
  <li><p><b>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </b></p></li>
  {% endfor %}{% endif %}{% endfor %}
</ul></div>

**1% Better**: It doesn't take much to get 1% better as a programmer. However, if we get 1% better two times a week, at the end of the year we'll be twice as good! This series covers tips and tricks that made me 1% better. Short, sweet, easy to read, easy to implement. [See All](../tags/#1%-Better)

<div class="posts-list"><ul>
  {% for tag in site.tags %}{% if tag[0] == "1% Better" %}{% assign posts = tag[1] | slice:0, 3 %}{% for post in posts %}
  <li><p><b>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </b></p></li>
  {% endfor %}{% endif %}{% endfor %}
</ul></div>