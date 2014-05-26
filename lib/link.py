#-*- coding: utf8 -*-

import os
import re
import logging

import settings
from lib.post import ALLOWED_PARSER
from lib.parser import Parser

class Link:
	def __init__(self, file='links.txt'):
		self.file = os.path.join(settings.DATA_DIR, file)

		self.parser = settings.PARSER
		self.content = ''

	def get(self):
		return self.content

	def parse(self):
		p = Parser(file=self.file, parser=self.parser)
		try:
			args = p.parse()

			self.content = args['content']
		except Exception, e:
			logging.warning("LINK %s" % (str(e)))
