#-*- coding: utf8 -*-

import os
import fnmatch
import re
import logging

ALLOWED_PARSER = ['mdown', 'plain']

class Parser:
	def __init__(self, file, parser = 'plain'):
		self.headers = ['title', 'parser', 'tags']
		self.parser = parser

		self.file = file
		self.args = {}

	def parse(self):
		"""
		Parse a file
		"""
		if not os.path.exists(self.file):
			raise Exception("File does not exist")

		self.args['content'] = ''
		self.args['url_title'] = os.path.splitext(os.path.basename(self.file))[0]
		self.args['date_ts'] = os.path.getmtime(self.file)

		for h in self.headers:
			self.args[h] = ''

		in_body = False
		for line in open(self.file, 'r'):
			if not in_body:
				m = re.search('^(' + '|'.join(self.headers) + '):(.*)', line)
				if m:
					header = m.group(1).strip()
					value = m.group(2).strip()
					if header == 'title':
						self.args['title'] = value
					elif header == 'parser' and value in ALLOWED_PARSER:
						self.args['parser'] = value
					elif header == 'tags':
						self.args['tags'] = map(lambda s: s.strip(), value.split(','))
				else: # A blank line in headers -> change to the post content
					in_body = True
			else:
				self.args['content'] += line

		if not self.parser == 'plain': # We need to parse the content
			if self.parser == 'mdown':
				try:
					from markdown import markdown
					self.args['content'] = markdown(self.args['content'])
				except ImportError, e:
					logging.warning("Markdown library does not exist")
				except Exception, e:
					logging.warning("%s" % (str(e)))
					# On error, do nothing, text will be displayed in plain format
					pass

		return self.args
