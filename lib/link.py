#-*- coding: utf8 -*-

import os
import re

import settings
from lib.post import ALLOWED_PARSER

class Link:
	def __init__(self, file='links.txt'):
		self.file = file

		self.parser = settings.PARSER
		self.content = ''

	def get(self):
		return self.content

	def parse(self):
		file = os.path.join(settings.DATA_DIR, self.file)
		if os.path.exists(file):
			in_body = False

			linksfile = open(file, 'r')
			for line in linksfile:
				if not in_body:
					m = re.search('^(parser):(:*)', line)
					if m:
						header = m.group(1).strip()
						value = m.group(2).strip()
						if header == 'parser' and value in ALLOWED_PARSER:
							self.parser = value
					else:
						in_body = True
						if not len(line.strip()) == 0: # We don't include headers in the file, so the first line is a data one
							self.content = line
				else:
					self.content += line

			if not self.parser == 'plain':
				if self.parser == 'mdown':
					try:
						from markdown import markdown
						self.content = markdown(self.content)
					except ImportError, e:
						print "ERROR: markdown library does not exist"
					except Exception, e:
						print "ERROR: %s" % (str(e))
						pass

			linksfile.close()
