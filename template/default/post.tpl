{% extends 'base.tpl' %}

{% block content %}
	<h2>{{post.title}}</h2>

	{{post.content}}
{% endblock %}
