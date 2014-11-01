{% extends 'base.tpl' %}

{% block content %}
	{% for p in posts %}
		<div class="article">
			<h2>
				<a href="{{base_url}}/{{p.url}}.html">
					{{p.date.strftime("[%d/%m/%Y]")}}&nbsp;{{p.title}}</h2>
				</a>
		</div>
	{% endfor %}
{% endblock %}
