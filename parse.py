#-*- coding: utf8 -*-
import sys
import os
import logging
from datetime import datetime

try:
	import settings
except:
	print("No config file found")
	sys.exit(1)

logging.basicConfig(
	format='%(asctime)s PYCMS %(levelname)s %(message)s',
	level=logging.DEBUG
)

from lib.post import PostsManager
from lib.function import save_tpl
from lib.static import move_static_files
from lib.link import Link
from lib.tag import TagManager

from jinja2 import Environment, FileSystemLoader

def main():
	if len(settings.DATA_DIR) == 0 or len(settings.OUT_DIR) == 0:
		logging.error("MAIN Please fill correctly the config file")
		sys.exit(1)

	if not os.path.isdir(settings.DATA_DIR):
		logging.error("MAIN Data dir '%s' does not exist" % (settings.DATA_DIR))
		sys.exit(1)

	if not os.path.isdir('template/%s' % (settings.WEBSITE_THEME)):
		logging.error("MAIN Theme '%s' does not exist" % (settings.WEBSITE_THEME))
		sys.exit(1)

	if not os.path.isdir(settings.OUT_DIR):
		try:
			os.mkdir(settings.OUT_DIR)
		except Exception as e:
			logging.error(str(e))
			sys.exit(1)

	posts = PostsManager()

	posts.generate_list()
	if len(posts.posts_list) == 0:
		logging.error("MAIN Please write some posts before doing a parse")
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
		'document_root': settings.WEBSITE_DOCUMENT_ROOT,
		'page_title': settings.WEBSITE_TITLE,
		'links': links.get(),
		'tags': ''
	}

	#
	# Posts generation
	#
	index_posts_list = []
	for post in posts.get_list():
		try:
			logging.info("MAIN Reading %s" % (post.file))
			post.parse()
		except Exception as e:
			logging.warning("MAIN %s" % (str(e)))
			continue

		index_posts_list.append({
			'title': post.title,
			'content': post.content,
			'url': post.url_title,
			'date': datetime.fromtimestamp(post.date_ts),
			'tags': post.tags
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
	# Tags Manager - Used to generate tags cloud
	#
	tagsmgr = TagManager()
	tagsmgr.parse(posts=index_posts_list)
	common_args['tags'] = tagsmgr.get_list()
	tagsmgr.save(tplenv=tplenv, extra_args=common_args)

	#
	# save posts files
	#
	posts.save(tplenv=tplenv, extra_args=common_args)

	#
	# generate and save the home page
	#
	_args = {
		'page_title': settings.WEBSITE_TITLE,
		'page_name': 'Accueil - liste des billets',
		'posts': index_posts_list
	}
	_args.update(common_args)
	save_tpl(
		tplenv=tplenv,
		args=_args,
		tplname='index.tpl',
		dst=os.path.join(settings.OUT_DIR, 'index.html')
	)

	#
	# Move static file (css, js, img, ...) from the template dir to the output dir
	#
	move_static_files(
		static_dir = os.path.join(theme_dir, 'static'),
		output_dir = os.path.join(settings.OUT_DIR, 'static')
	)

if __name__ == "__main__":
	main()
