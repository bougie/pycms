#-*- coding: utf8 -*-
import os

class Category:
	def __init__(self):
		self.items = []
		self.flat_items = dict()

	def get(category_id):
		"""
		Get the category name by the category id
		"""
		try:
			return self.flat_items[cid]
		except:
			return None

	def get_all(self):
		"""
		Return the categories tree
		"""
		return self.items

	def list_items(self):
		"""
		Return the flat tree of categories
		"""
		return self.flat_items

	def _parse(self, path):
		"""
		Generate categories tree
		"""
		items = []
		_items = os.listdir(path)

		for item in _items:
			npath = os.path.join(path, item)
			if os.path.isdir(npath):
				t = item.split('-')

				if len(t) > 1:
					cat = {
						'id': t[1],
						'name': t[0],
						'subcat': self._parse(path=npath)
					}

					items.append(cat)
					self.flat_items[t[1]] = t[0]

		return items

	def parse(self, path):
		self.items = self._parse(path=path)
