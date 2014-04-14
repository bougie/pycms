#-*- coding: utf8 -*-

class TagManager:
	def __init__(self):
		self.tags = {}

	def add(self, tag, post):
		if not tag in self.tags:
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
