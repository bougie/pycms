{% extends 'base.tpl' %}

{% block content %}
	<h2>{{post.title}}</h2>

	{{post.content}}

	{% if post.author %}
		<span class="author">Ecrit par {{post.author}}</span>
	{% endif %}
{% endblock %}
