<!DOCTYPE html>
<html lang="fr">
 	<head>
		<title>{{page_title}}</title>
		<meta charset="utf-8">

		<meta name="author" content="{{page_author}}" />
		<meta name="keywords" content="{{page_keywords}}" />
		<meta name="description" content="{{page_description}}" />

		<link rel="stylesheet" href="{{base_url}}/static/css/style.css" />

		{% if activate_rss %}
			<link rel="alternate" type="application/rss+xml" title="RSS" href="{{rss}}" />
		{% endif %}
	</head>
	<body>
		<div id="page">
			<div id="header">
				<h1><a href="{{base_url}}/index.html">{{page_title}}</a></h1>
			</div>

			<div id="content">
				{% block content %}
				{% endblock %}
			</div>

			<div id="menu">
				<h2>SITE</h2>
				<ul>
					<li><a href="{{base_url}}/index.html">Accueil</a></li>
				</ul>
				{% if links %}
					<h2>LIENS</h2>
					{{links}}
				{% endif %}
				
				{% if tags|length > 0 %}
					<h2>TAGS</h2>
					{% for tag in tags %}
						<a href="{{base_url}}/tags/{{tag}}.html">{{tag}}</a>
					{% endfor %}
				{% endif %}
				{% if activate_rss %}
					<br /><br />
					<a type="application/rss+xml" href="{{rss}}">
						<img src="{{base_url}}/static/img/rss.jpg" alt="RSS" />
					</a> 
				{% endif %}
			</div>

			<div class="footer">
				Copyright © 2014. Tous droits réservés.<br />
				Toute reproduction partielle ou totale de ce site est vivement conseillée avec ou sans l'accord écrit de l'éditeur (ou pas). 
			</div>
		</div>
	</body>
</html>
