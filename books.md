---
layout: page
title: books
permalink: /books/
---

# The Latest from The Data-Sitters Club

Be sure to also check out our <a href="#mystery">multilingual mystery series</a>!

{% for post in site.posts reversed %}
{% if post.bookseries contains "regular" %}
<a href="/site/{{ post.url }}"><img src="/site/assets/bookcovers/{{ post.coverart }}" /></a>
<h3 class="postlist"><a href="/site/{{ post.url }}">{{ post.title }}</a></h3>
<p class="postlist">{{ post.author }}</p>
<p class="postlist">{{ post.date | date_to_long_string }}</p>
<p class="postlist">{{ post.blurb }}</p>	
<br />	
{% endif %}	
{% endfor %}

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