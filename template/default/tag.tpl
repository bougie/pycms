{% extends 'base.tpl' %}

{% block name %}
<h2>NOM</h2>
<div class="name_content">
	{{page_name}}
</div>
{% endblock %}

{% block content %}
<h2>BILLETS</h2>
<div class="content_content">
	<ul>
		{% for p in posts %}
			<li>
				<a href="{{p.url}}.html">
					{{p.date.strftime("%Y-%m-%d")}}&nbsp;-&nbsp;{{p.title}}
				</a>
			</li>
		{% endfor %}
	</ul>
</div>
{% endblock %}
