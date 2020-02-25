---
layout: page
title: books
permalink: /books/
---

# The Data-Sitters Club Books

## Main series

Be sure to also check out our <a href="#mystery">multilingual mystery series</a>!

| [![DSC #1 Quinn's Great Idea](https://raw.githubusercontent.com/datasittersclub/site/master/assets/bookcovers/dsc1_cover.jpg)]() | [![DSC #2 Katia and the Phantom Corpus](https://raw.githubusercontent.com/datasittersclub/site/master/assets/bookcovers/dsc2_cover.jpg)]() | [![DSC #3 The Truth About Digital Humanities Collaborations](https://raw.githubusercontent.com/datasittersclub/site/master/assets/bookcovers/dsc3_cover.jpg)](http://graphicstock.com) |
| :------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                   DSC #1 - Quinn's Great Idea                                                    |                                                   DSC #2 - Katia and the Phantom Corpus                                                    |                                                               DSC #3 - The Truth About Digital Humanities Collaborations                                                               |

<a name="mystery" />
## Multilingual Mysteries

{% for post in site.posts reversed %}
{% if post.bookseries contains "mystery" %}
<a href="/site/{{ post.url }}"><img src="/site/assets/bookcovers/{{ post.coverart }}" /></a>

<h3 class="postlist"><a href="/site/{{ post.url }}">{{ post.title }}</a></h3>
<p class="postlist">{{ post.author }}</p>
<p class="postlist">{{ post.date | date_to_long_string }}</p>
<p class="postlist">{{ post.blurb }}</p>
<br />
{% endif %}
{% endfor %}
