---
layout: post
title:  "Farseer Review"
date:   2023-08-21 10:15:00 +0100
categories: [jekyll update, test]
---
jhnb 
![image tooltip here](/assets/images/23-08-21-farseer-review/farseer-trilogy.jpeg)

{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}