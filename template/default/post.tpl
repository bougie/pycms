{% extends 'base.tpl' %}

{% block content %}
<h2>{{post.title}}</h2>

<div class="post_content">
	{{post.content}}
</div>
{% endblock %}
