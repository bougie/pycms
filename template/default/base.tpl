<!DOCTYPE html>
<html lang="fr">
 	<head>
		<title>{{page_title}}</title>
		<meta charset="utf-8">

		<link rel="stylesheet" href="{{document_root}}static/css/style.css" />

		<link rel="alternate" type="application/rss+xml" title="RSS" href="{{rss}}" />
	</head>
	<body>
		<h1><a href="{{document_root}}index.html">{{page_title}}</a></h1>

		<div class="name">
		{% block name %}
		{% endblock %}
		</div>

		<div class="content">
		{% block content %}
		{% endblock %}
		</div>

		{% if tags|length > 0 %}
			<div class="tagscloud">
				<h2>TAGS</h2>
				<div class="tagscloud_content">
				{% for tag in tags %}
					<a href="{{document_root}}tags/{{tag}}.html">{{tag}}</a>
				{% endfor %}
				</div>
			</div
		{% endif %}

		{% if links %}
			<div class="seealso">
				<h2>A VOIR</h2>
				<div class="seealso_content"
					{{links}}
				</div>
			</div>
		{% endif %}
		<div class="footer">
			<h2>Pied de page</h2>
			<a type="application/rss+xml" href="{{rss}}">
				Flux RSS des billets
			</a> 
		</div>
	</body>
</html>
