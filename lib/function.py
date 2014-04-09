#-*- coding: utf8 -*-

def save_file(path, content):
	try:
		fh = open(path, 'w+')
		fh.write(content)
		fh.close()
	except Exception, e:
		print 'ERROR: ' + str(e)
