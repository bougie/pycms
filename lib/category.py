#-*- coding: utf8 -*-
import os

import settings

class Category:
	items_tree = []
	items_list = dict()

	def __init__(self, id=None, name=None, path=None, children=None):
		self.id = id
		self.name = name
		self.path = path
		self.children = children

	def get(self, category_id):
		"""
		Get the category name by the category id
		"""
		try:
			return Category.items_list[category_id]
		except:
			return None

	def generate_subtree(self, path):
		items = []
		_items = os.listdir(path)

		for item in _items:
			npath = os.path.join(path, item)
			if os.path.isdir(npath):
				t = item.split('-')

				if len(t) > 1:
					cat = Category(
						id=t[1],
						name=t[0],
						path=npath,
						children=self.generate_subtree(path=npath))

					items.append(cat)
					Category.items_list[t[1]] = t[0]

		return items

	def generate_tree(self):
		"""
		Generate categories tree
		"""
		Category.iems_tree = self.generate_subtree(path=settings.DATA_DIR)
