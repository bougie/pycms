#-*- coding: utf8 -*-

import os
import fnmatch
import re
import logging
import time

from lib.wrap import wrap
import settings

ALLOWED_PARSER = ['mdown', 'plain']

class Parser:
	def __init__(self, file, parser = 'plain'):
		self.headers = ['title', 'parser', 'tags', 'author', 'date']
		self.parser = parser

		self.file = file
		self.args = {}

	"""
	Parse text to replace content vars with settings parameter
	"""
	def add_settings_vars(self, text):
		vars = {
			'media_url': settings.WEBSITE_MEDIA_URL
		}

		for k, v in vars.items():
			text = text.replace('{{%s}}' % (k), v)

		return text

	"""
	Parse a file
	"""
	def parse(self):
		if not os.path.exists(self.file):
			raise IOError("File %s does not exist" % (self.file))

		self.args['content'] = ''
		self.args['small_content'] = ''
		self.args['url_title'] = os.path.splitext(os.path.basename(self.file))[0]
		self.args['date_ts'] = os.path.getmtime(self.file)
		self.args['author'] = None

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
					elif header == 'author':
						self.args['author'] = value
					elif header == 'date':
						try:
							self.args['date_ts'] = time.mktime(
								time.strptime(value, '%Y-%m-%d %H:%M')
							)
						except Exception as e:
							# On error, keep the last modified ts of the file
							logging.info('PARSER %s' % (str(e)))
				else: # A blank line in headers -> change to the post content
					in_body = True
			else:
				self.args['content'] += line

		self.args['content'] = self.add_settings_vars(self.args['content'])

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
