#-*- coding: utf8 -*-
import os
import fnmatch
import re

class Post:
	def __init__(self):
		self.posts = []

	def get_all(self):
		"""
		Get all posts
		"""
		return self.posts

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
						post = {
							'category': t[1],
							'file': mdfile
						}
						items.append(post)

		return items

	def generate_list(self, path):
		self.posts = self._list(path=path)

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
