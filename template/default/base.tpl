<!DOCTYPE html>
<html lang="fr">
 	<head>
		<title>{{page_title}}</title>
		<meta charset="utf-8">
	</head>
	<body>
		<h1>{{page_title}}</h1>

		<div class="name">
		{% block name %}
		{% endblock %}
		</div>

		<div class="content">
		{% block content %}
		{% endblock %}
		</div>

		<div class="seealso">
			<h2>A voir</h2>
			{{links}}
		</div>
	</body>
</html>
