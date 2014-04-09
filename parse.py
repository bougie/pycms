#-*- coding: utf8 -*-
import sys
import os

try:
	import settings
except:
	print "ERROR: No config file found"
	sys.exit(1)

from lib.post import PostsManager
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

posts = PostsManager()

posts.generate_list()
if len(posts.posts_list) == 0:
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
		print "Reading %s" % (post.file)
		post.parse()
	except Exception, e:
		print "    %s" % (str(e))
		continue

	index_posts_list.append({
		'title': post.title,
		'content': post.content
	})

args = {
	'page_title': 'TAW - The Appartland Website',
	'page_name': 'Accueil - liste des billets',
	'posts': index_posts_list
}
hometpl = tplenv.get_template(name='index.tpl')
hometpl_content = hometpl.render(args)
save_file(path=os.path.join(settings.OUT_DIR, 'index.html'), content=hometpl_content)
