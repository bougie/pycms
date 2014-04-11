{% extends 'base.tpl' %}

{% block name %}
<h2>NAME</h2>
{{page_name}}
{% endblock %}

{% block content %}
<h2>BILLETS</h2>
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
