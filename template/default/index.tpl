{% extends 'base.tpl' %}

{% block content %}
{% for p in posts %}
	<div class="post">
		{% if p.category %}
			<h2>[{{p.category}}] {{p.title}}</h2>
		{% else %}
			<h2>{{p.title}}</h2>
		{% endif %}

		<div>{{p.content}}</div>
	</div>
{% endfor %}
{% endblock %}
