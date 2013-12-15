#-*- coding: utf8 -*-
import os
import fnmatch

class Post:
	def __init__(self):
		self.posts = []

	def get_all(self):
		"""
		Get all posts
		"""
		return self.posts

	def _parse(self, path, dirname = '', items = []):
		"""
		Generate posts tree
		"""
		_items = os.listdir(path)
		for item in _items:
			npath = os.path.join(path, item)
			if os.path.isdir(npath):
				items = self._parse(path=npath, dirname=item, items=items)
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

	def parse(self, path):
		self.posts = self._parse(path=path)
