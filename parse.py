#-*- coding: utf8 -*-
import sys
import os

try:
	import settings
except:
	print "ERROR: No config file found"
	sys.exit(1)

from function.category import Category
from function.post import Post

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

posts.generate_list()
if len(Post.posts_list) == 0:
	print "ERROR: please write some posts before doing a parse"
	sys.exit(1)

"""posts_list = []
for post in posts.get_all():
	try:
		p = posts.parse(path=post['file'], category=post['category'])
	except:
		p = None

	if p:
		posts_list.append(p)"""
