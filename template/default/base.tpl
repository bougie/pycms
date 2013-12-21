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

		<h2>DESCRIPTION</h2>
		<div class="content">
		{% block content %}
		{% endblock %}
		</div>

		<div class="menu">
			<h2>Categories</h2>
			<ul>
			{% for cat in categories %}
				<li>{{cat.name}}</li>
			{% endfor %}
			</ul>
		</div>
	</body>
</html>
