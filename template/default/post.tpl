{% extends 'base.tpl' %}

{% block name %}
<h2>TITRE</h2>
{{post.title}}
{% endblock %}

{% block content %}
<h2>DESCRIPTION</h2>
{{post.content}}
{% endblock %}
