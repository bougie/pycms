#-*- coding: utf8 -*-
import os
import fnmatch
import re

import settings
from lib.function import save_file

ALLOWED_PARSER = ['mdown', 'plain']

class PostsManager:
	def __init__(self, file=None):
		self.posts_list = []

	def _list(self, path, dirname = ''):
		"""
		Generate posts tree
		"""
		_items = os.listdir(path)
		for item in _items:
			npath = os.path.join(path, item)
			if os.path.isdir(npath):
				self._list(path=npath, dirname=item)
			else:
				bpfile = os.path.join(path, item)
				if fnmatch.fnmatch(bpfile, '*.bp'):
					self.posts_list.append(Post(file=bpfile))

	def generate_list(self):
		"""
		Generate posts tree
		"""
		self._list(path=settings.DATA_DIR)

class Post:
	def __init__(self, file):
		self.file = file
		self.parser = settings.PARSER

		self.title = ''
		self.content = ''
		self.url_title = ''
		self.date_ts = 0

		self.set_url_title()

	def set_url_title(self):
		"""
		Set the post title shown in the URL
		"""
		self.url_title = os.path.splitext(os.path.basename(self.file))[0]

	def parse(self):
		"""
		Parse a post file
		"""
		if not os.path.exists(self.file):
			raise Exception("Post file does not exist")

		self.date_ts = os.path.getmtime(self.file)

		in_body = False

		postfile = open(self.file, 'r')
		for line in postfile:
			#line = line.rstrip('\n\r').rstrip('\n')

			if not in_body:
				m = re.search('^(title|parser):(.*)', line)
				if m:
					header = m.group(1).strip()
					value = m.group(2).strip()
					if header == 'title':
						self.title = value
					elif header == 'parser' and value in ALLOWED_PARSER:
						self.parser = value
				else: # A blank line in headers -> change to the post content
					in_body = True
			else:
				self.content += line

		if not self.parser == 'plain': # We need to parse the content
			if self.parser == 'mdown':
				try:
					from markdown import markdown
					self.content = markdown(self.content)
				except ImportError, e:
					print "ERROR: makdown library does not exist"
				except Exception, e:
					print "ERROR: %s" % (str(e))
					# On error, do nothing, text will be displayed in plain format
					pass

		postfile.close()

	def save(self, tplenv):
		"""
		Save post content into an HTML file
		"""
		args = {
			'page_title': settings.WEBSITE_TITLE,
			'page_name': 'Billet - Lecture',
			'post': {
				'title': self.title,
				'content': self.content
			}
		}
		tpl = tplenv.get_template(name='post.tpl')
		tpl_content = tpl.render(args)
		save_file(path=os.path.join(settings.OUT_DIR, '%s.html' % (self.url_title)), content=tpl_content)
