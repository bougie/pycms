#-*- coding: utf8 -*-

def save_file(path, content):
	try:
		fh = open(path, 'a+')
		fh.write(content)
		fh.close()
	except Exception, e:
		print 'ERROR: ' + str(e)
