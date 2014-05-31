#-*- coding: utf8 -*-
import os
import fnmatch
import re
import logging
from datetime import datetime

import settings
from lib.function import save_tpl
from lib.parser import Parser

ALLOWED_PARSER = ['mdown', 'plain']

class PostsManager:
	def __init__(self, file=None):
		self.posts_list = []
		self.recent_date = None

	def generate_list(self, path, dirname = ''):
		"""
		Generate posts tree
		"""
		_items = os.listdir(path)
		for item in _items:
			npath = os.path.join(path, item)
			if os.path.isdir(npath):
				self.generate_list(path=npath, dirname=item)
			else:
				bpfile = os.path.join(path, item)
				if fnmatch.fnmatch(bpfile, '*.bp'):
					self.posts_list.append(Post(file=bpfile))

	def get_last_post_date(self):
		"""
		Get the last post date. Posts need to be parsed before
		"""
		return self.recent_date

	def get_list(self):
		return self.posts_list

	def parse(self):
		"""
		Parse all posts from the posts list
		"""
		posts_list = []
		for post in self.posts_list:
			try:
				logging.info("POSTS Reading %s" % (post.file))
				post.parse()
			except Exception as e:
				logging.warning("POSTS %s" % (str(e)))
				# On error do not add into the list
				# but continue with others posts
				continue

			posts_list.append({
				'title': post.title,
				'content': post.content,
				'description': post.small_content,
				'url': post.url_title,
				'date': datetime.fromtimestamp(post.date_ts),
				'tags': post.tags
			})
			
			if not self.recent_date is None:
				self.recent_date = max(self.recent_date, post.date_ts)
			else:
				self.recent_date = post.date_ts
		return posts_list

	def save(self, tplenv, extra_args={}):
		"""
		Save all posts into a file
		"""
		for post in self.posts_list:
			try:
				logging.info("POSTS Saving %s in %s" % (
					post.file, post.url_title)
				)
				post.save(tplenv=tplenv, extra_args=extra_args)
			except Exception as e:
				logging.warning("POSTS %s" % (str(e)))
				continue

class Post:
	def __init__(self, file):
		self.file = file
		self.parser = settings.PARSER

		self.title = ''
		self.content = ''
		self.small_content = ''
		self.url_title = ''
		self.date_ts = 0
		self.tags = ''

	def parse(self):
		"""
		Parse a post file
		"""
		p = Parser(file=self.file, parser=self.parser)
		try:
			args = p.parse()

			self.title = args['title']
			self.content = args['content']
			self.small_content = args['small_content']
			self.url_title = args['url_title']
			self.date_ts = args['date_ts']
			self.tags = args['tags']
		except Exception as e:
			logging.warning("POST %s" % (str(e)))

	def save(self, tplenv, extra_args={}):
		"""
		Save post content into an HTML file
		"""
		_args = {
			'page_name': 'Billet - Lecture',
			'post': {
				'title': self.title,
				'content': self.content
			}
		}
		_args.update(extra_args)

		save_tpl(
			tplenv=tplenv,
			args=_args,
			tplname='post.tpl',
			dst=os.path.join(settings.OUT_DIR, '%s.html' % (self.url_title))
		)
