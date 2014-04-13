{% extends 'base.tpl' %}

{% block name %}
<h2>NOM</h2>
<div class="name_content">
	{{post.title}}
</div>
{% endblock %}

{% block content %}
<h2>DESCRIPTION</h2>
<div class="content_content">
	{{post.content}}
</div>
{% endblock %}
