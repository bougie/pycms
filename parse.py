#-*- coding: utf8 -*-
import sys
import os

try:
	import settings
except:
	print "ERROR: No config file found"
	sys.exit(1)

from lib.category import Category
from lib.post import Post
from lib.function import save_file

from jinja2 import Environment, FileSystemLoader

if len(settings.DATA_DIR) == 0 or len(settings.OUT_DIR) == 0:
	print "ERROR: Please fill correctly the config file"
	sys.exit(1)

if not os.path.isdir(settings.DATA_DIR):
	print "ERROR: Data dir '%s' does not exist" % (settings.DATA_DIR)
	sys.exit(1)

if not os.path.isdir(settings.OUT_DIR):
	try:
		os.mkdir(settings.OUT_DIR)
	except Exception, e:
		print "ERROR: " + str(e)
		sys.exit(1)

categories = Category()
posts = Post()

categories.generate_tree()
if len(Category.items_list) == 0:
	print "ERROR: please create some categories before doing a parse"
	sys.exit(1)

cats_list = []
for cat_name in Category.items_list.values():
	cats_list.append({
		'name': cat_name
	})

posts.generate_list()
if len(Post.posts_list) == 0:
	print "ERROR: please write some posts before doing a parse"
	sys.exit(1)

tplenv = Environment()
tplenv.loader = FileSystemLoader('template/default')

#
# Home page (index.html) generation
#
index_posts_list = []
for post in posts.posts_list:
	try:
		post.parse()
	except:
		continue

	index_posts_list.append({
		'category': categories.get(category_id=post.category),
		'title': post.title,
		'content': post.content
	})

args = {
	'page_title': 'TAW - The Appartland Website',
	'page_name': 'Accueil - liste des billets',
	'categories': cats_list,
	'posts': index_posts_list
}
hometpl = tplenv.get_template(name='index.tpl')
hometpl_content = hometpl.render(args)
save_file(path=os.path.join(settings.OUT_DIR, 'index.html'), content=hometpl_content)
