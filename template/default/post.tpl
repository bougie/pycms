{% extends 'base.tpl' %}

{% block content %}
	<div class="article">
		<h2>{{post.title}}</h2>

		{{post.content}}

		<div class="article_infos">
			<span class="author_date">
				Ecrit
				{% if post.author %}
					par {{post.author}}
				{% endif %}
				{% if post.date %}
					le {{post.date.strftime("%d/%m/%Y à %H:%M")}}
				{% endif %}
			</span>
			<div class="tags">
				Tags:&nbsp;
				{% for tag in post.tags %}
					<a href="{{base_url}}/tags/{{tag}}.html">{{tag}}</a>
				{% endfor %}
			</div>
		</div>
	</div>
{% endblock %}
