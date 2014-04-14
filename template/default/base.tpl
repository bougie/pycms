<!DOCTYPE html>
<html lang="fr">
 	<head>
		<title>{{page_title}}</title>
		<meta charset="utf-8">

		<link rel="stylesheet" href="static/css/style.css" />
	</head>
	<body>
		<h1><a href="index.html">{{page_title}}</a></h1>

		<div class="name">
		{% block name %}
		{% endblock %}
		</div>

		<div class="content">
		{% block content %}
		{% endblock %}
		</div>

		<div class="tagscloud">
			<h2>TAGS</h2>
			<div class="tagscloud_content">
			{% for tag in tags %}
				<a href="tags/{{tag}}.html">{{tag}}</a>
			{% endfor %}
			</div>
		</div>

		<div class="seealso">
			<h2>A VOIR</h2>
			<div class="seealso_content"
				{{links}}
			</div>
		</div>
	</body>
</html>
