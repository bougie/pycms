#-*- coding: utf8 -*-
import logging

def save_file(path, content):
	try:
		fh = open(path, 'w+')
		fh.write(content)
		fh.close()
	except Exception as e:
		logging.error('SAVE %s' % (str(e)))

def save_tpl(tplenv, args, tplname, dst):
	tpl = tplenv.get_template(name=tplname)
	tpl_content = tpl.render(args)
	save_file(path=dst, content=tpl_content)
