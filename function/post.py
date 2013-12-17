#-*- coding: utf8 -*-
import os
import fnmatch
import re

import settings

class Post:
	posts_list = []

	def __init__(self, file=None, category=None):
		self.category = category
		self.file = file

		self.title = ''
		self.content = ''

	def _list(self, path, dirname = '', items = []):
		"""
		Generate posts tree
		"""
		_items = os.listdir(path)
		for item in _items:
			npath = os.path.join(path, item)
			if os.path.isdir(npath):
				items = self._list(path=npath, dirname=item, items=items)
			else:
				mdfile = os.path.join(path, item)
				if fnmatch.fnmatch(mdfile, '*.md'):
					t = dirname.split('-')
			
					if len(t) > 1:
						items.append(Post(file=mdfile, category=t[1]))

		return items

	def generate_list(self):
		"""
		Generate posts tree
		"""
		Post.posts_list = self._list(path=settings.DATA_DIR)

	def parse(self, path, category = None):
		"""
		Parse a post file
		"""
		if not os.path.exists(path):
			raise Exception("Post file does not exist")

		in_body = False
		post = {
			'category': category,
			'title': '',
			'content': ''
		}

		postfile = open(path, 'r')
		for line in postfile:
			#line = line.rstrip('\n\r').rstrip('\n')

			if not in_body:
				m = re.search('^title:(.*)', line)
				if m:
					post['title'] = m.group(1).strip()
				else:
					in_body = True
			else:
				post['content'] += line

		postfile.close()

		return post
