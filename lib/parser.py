#-*- coding: utf8 -*-

import os
import fnmatch
import re
import logging

from lib.wrap import wrap

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
			raise IOError("File %s does not exist" % (self.file))

		self.args['content'] = ''
		self.args['small_content'] = ''
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
						self.parser = value
					elif header == 'tags':
						self.args['tags'] = list(
							map(lambda s: s.strip(), value.split(','))
						)
				else: # A blank line in headers -> change to the post content
					in_body = True
			else:
				self.args['content'] += line

		self.args['small_content'] = wrap(content=self.args['content'])

		if not self.parser == 'plain': # We need to parse the content
			if self.parser == 'mdown':
				try:
					from markdown import markdown
					self.args['content'] = markdown(self.args['content'])
					self.args['small_content'] = markdown(
						self.args['small_content']
					)
				except ImportError as e:
					logging.warning("PARSER Markdown library does not exist")
				except Exception as e:
					logging.warning("PARSER %s" % (str(e)))
					# On error, do nothing, text will be displayedi
					# in plain text
					pass

		return self.args
