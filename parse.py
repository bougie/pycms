#-*- coding: utf8 -*-
import sys
import os
from datetime import datetime

try:
	import settings
except:
	print "ERROR: No config file found"
	sys.exit(1)

from lib.post import PostsManager
from lib.function import save_file
from lib.static import move_static_files
from lib.link import Link

from jinja2 import Environment, FileSystemLoader

if len(settings.DATA_DIR) == 0 or len(settings.OUT_DIR) == 0:
	print "ERROR: Please fill correctly the config file"
	sys.exit(1)

if not os.path.isdir(settings.DATA_DIR):
	print "ERROR: Data dir '%s' does not exist" % (settings.DATA_DIR)
	sys.exit(1)

if not os.path.isdir('template/%s' % (settings.WEBSITE_THEME)):
	print "ERROR: Theme '%s' does not exist" % (settings.WEBSITE_THEME)
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

theme_dir = 'template/%s' % (settings.WEBSITE_THEME)

tplenv = Environment()
tplenv.loader = FileSystemLoader(theme_dir)

#
# Generate links
#
links = Link()
links.parse()

common_args = {
	'page_title': settings.WEBSITE_TITLE,
	'links': links.get()
}

#
# Posts generation
#
index_posts_list = []
for post in posts.posts_list:
	try:
		print "Reading %s" % (post.file)
		post.parse()

		print "Saving %s in %s" % (post.file, post.url_title)
		post.save(tplenv=tplenv, extra_args=common_args)
	except Exception, e:
		print "    %s" % (str(e))
		continue

	index_posts_list.append({
		'title': post.title,
		'content': post.content,
		'url': post.url_title,
		'date': datetime.fromtimestamp(post.date_ts)
	})

#
# Sort posts list on the home page
#
sort = 'date' # sort by date by default
sort_revers_order = True # sort in revers order by default
usersort = settings.POSTS_SORT.split('-')
if len(usersort) == 2:
	if usersort[0] in ['date', 'title']: #Allowed sort filter
		sort = usersort[0]
		if usersort[1] == 'ASC':
			sort_revers_order = False
		elif usersort == 'DESC':
			sort_revers_order = True

index_posts_list = sorted(
	index_posts_list,
	key=lambda pst: pst[sort],
	reverse=sort_revers_order
)

#
# generate and save the home page
#
_args = {
	'page_title': settings.WEBSITE_TITLE,
	'page_name': 'Accueil - liste des billets',
	'posts': index_posts_list
}
args = dict(_args.items() + common_args.items())
hometpl = tplenv.get_template(name='index.tpl')
hometpl_content = hometpl.render(args)
save_file(path=os.path.join(settings.OUT_DIR, 'index.html'), content=hometpl_content)

#
# Move static file (css, js, img, ...) from the template dir to the output dir
#
move_static_files(
	static_dir = os.path.join(theme_dir, 'static'),
	output_dir = os.path.join(settings.OUT_DIR, 'static')
)
