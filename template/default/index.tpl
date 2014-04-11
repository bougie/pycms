{% extends 'base.tpl' %}

{% block content %}
<ul>
	{% for p in posts %}
		<li>
			<a href="{{p.url}}.html">
				{{p.date.strftime("%Y-%m-%d")}}&nbsp;-&nbsp;{{p.title}}
			</a>
		</li>
	{% endfor %}
</ul>
{% endblock %}
