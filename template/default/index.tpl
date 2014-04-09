{% extends 'base.tpl' %}

{% block content %}
<ul>
	{% for p in posts %}
		<li>{{p.title}}</li>
	{% endfor %}
</ul>
{% endblock %}
