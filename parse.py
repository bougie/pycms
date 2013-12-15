#-*- coding: utf8 -*-
import sys
import os

try:
	import settings
except:
	print "ERROR: No config file found"
	sys.exit(1)

if len(settings.DATA-DIR) == 0 or len(settings.OUT_DIR) == 0:
	print "ERROR: Please fill correctly the config file"
	sys.exit(1)

if not os.path.isdir(settings.DATA-DIR):
	print "ERROR: Data dir %s does not exist" % (settings.DATA-DIR)
	sys.exit(1)

if not os.path.isdir(settings.OUT_DIR):
	try:
		os.mkdir(settings.OUT_DIR)
	except Exception, e:
		print "ERROR: " + str(e)
		sys.exit(1)
