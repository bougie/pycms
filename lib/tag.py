#-*- coding: utf8 -*-

import os

from lib.function import save_tpl

import settings

class TagManager:
	def __init__(self):
		self.tags = {}

	def add(self, tag, post):
		if not tag in self.tags.keys():
			self.tags[tag] = []

		self.tags[tag].append(post)

	def get_list(self):
		"""
		Return dict keys as the tag list cause keys are uniq in a dict
		"""
		return self.tags.keys()

	def parse(self, posts):
		for post in posts:
			for tag in post['tags']:
				self.add(tag=tag, post=post)

	def save(self, tplenv, extra_args):
		"""
		Generate each pages which contain posts list associated with a tag
		"""
		tagdir = os.path.join(settings.OUT_DIR, 'tags')
		if not os.path.isdir(tagdir):
			os.mkdir(tagdir)

		for tagname in self.get_list():
			_args = {
				'page_name': 'TAG %s - Liste des billets' % (tagname),
				'posts': self.tags[tagname]
			}
			_args.update(extra_args)

			save_tpl(
				tplenv=tplenv,
				args=_args,
				tplname='tag.tpl',
				dst=os.path.join(tagdir, '%s.html' % tagname)
	        )
