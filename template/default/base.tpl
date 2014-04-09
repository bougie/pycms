<!DOCTYPE html>
<html lang="fr">
 	<head>
		<title>{{page_title}}</title>
		<meta charset="utf-8">
	</head>
	<body>
		<h1>{{page_title}}</h1>

		<h2>NOM</h2>
		<div class="name">{{page_name}}</div>

		<h2>BILLETS</h2>
		<div class="content">
		{% block content %}
		{% endblock %}
		</div>
	</body>
</html>
