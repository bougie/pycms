#-*- coding: utf8 -*-
import os
import fnmatch
import re
import logging

import settings
from lib.function import save_tpl
from lib.parser import Parser

ALLOWED_PARSER = ['mdown', 'plain']

class PostsManager:
	def __init__(self, file=None):
		self.posts_list = []

	def _list(self, path, dirname = ''):
		"""
		Generate posts tree
		"""
		_items = os.listdir(path)
		for item in _items:
			npath = os.path.join(path, item)
			if os.path.isdir(npath):
				self._list(path=npath, dirname=item)
			else:
				bpfile = os.path.join(path, item)
				if fnmatch.fnmatch(bpfile, '*.bp'):
					self.posts_list.append(Post(file=bpfile))

	def generate_list(self):
		"""
		Generate posts tree
		"""
		self._list(path=settings.DATA_DIR)

class Post:
	def __init__(self, file):
		self.file = file
		self.parser = settings.PARSER

		self.title = ''
		self.content = ''
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
			self.url_title = args['url_title']
			self.date_ts = args['date_ts']
			self.tags = args['tags']
		except Exception, e:
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

		save_tpl(
			tplenv=tplenv,
			args=dict(_args.items() + extra_args.items()),
			tplname='post.tpl',
			dst=os.path.join(settings.OUT_DIR, '%s.html' % (self.url_title))
		)
