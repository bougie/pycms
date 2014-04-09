#-*- coding: utf8 -*-
import os
import fnmatch
import re

import settings

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
				mdfile = os.path.join(path, item)
				if fnmatch.fnmatch(mdfile, '*.md'):
					self.posts_list.append(Post(file=mdfile))

	def generate_list(self):
		"""
		Generate posts tree
		"""
		self._list(path=settings.DATA_DIR)

class Post:
	def __init__(self, file):
		self.file = file

		self.title = ''
		self.content = ''

	def parse(self):
		"""
		Parse a post file
		"""
		if not os.path.exists(self.file):
			raise Exception("Post file does not exist")

		self.title = ''
		self.content = ''

		in_body = False

		postfile = open(self.file, 'r')
		for line in postfile:
			#line = line.rstrip('\n\r').rstrip('\n')

			if not in_body:
				m = re.search('^title:(.*)', line)
				if m:
					self.title = m.group(1).strip()
				else:
					in_body = True
			else:
				self.content += line

		postfile.close()
