#-*- coding: utf8 -*-
import logging
import PyRSS2Gen
import os
from datetime import datetime

import settings

"""Manage RSS feed"""
class RSS:
	def __init__(self, title, description = '', link = '', file='feed'):
		self.file = os.path.join(settings.OUT_DIR, file)

		self.title = title
		self.description = description
		self.link = link

		self.items = []

	"""Add a items into the items list"""
	def add_item(self, link, title, description, date):
		try:
			self.items.append(PyRSS2Gen.RSSItem(
				link = link,
				title = title,
				description = description,
				guid = PyRSS2Gen.Guid(link),
				pubDate = date
			))
		except Exception as e:
			logging.warning('RSS unable to add item : %s' % (str(e)))

	"""Save the feed into the out dir"""
	def save(self, date = None):
		if not date is None:
			_date = datetime.fromtimestamp(date)
		else:
			_date = datetime.now()

		try:
			rss = PyRSS2Gen.RSS2(
				link=self.link,
				title=self.title,
				description=self.description,
				items=self.items,
				lastBuildDate=_date,
				pubDate=_date,
				language='fr_FR',
				docs=None
			)
			rss.write_xml(open(self.file, "w"), encoding='UTF-8')
		except Exception as e:
			logging.warning("RSS %s" % (str(e)))
