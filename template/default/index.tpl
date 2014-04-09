{% extends 'base.tpl' %}

{% block content %}
<ul>
	{% for p in posts %}
		<li><a href="{{p.url}}.html">{{p.title}}</a></li>
	{% endfor %}
</ul>
{% endblock %}
