{% extends 'base.tpl' %}

{% block content %}
	{% for p in posts %}
		<div class="article">
			<h2>{{p.date.strftime("[%d/%d/%Y]")}}&nbsp;{{p.title}}</h2>

			<div>
				{{p.description}}<a href="{{base_url}}/{{p.url}}.html">Lire la suite</a>
			</div>
		</div>
	{% endfor %}
{% endblock %}
