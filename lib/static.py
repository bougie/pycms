#-*- coding: utf8 -*-
import os
import shutil
import logging

def move_files(input_dir, output_dir):
	try:
		if os.path.isdir(output_dir):
			shutil.rmtree(output_dir)

		if os.path.exists(input_dir):
			os.mkdir(output_dir)

			items = os.listdir(input_dir)
			for item in items:
				tmpitem = os.path.join(input_dir, item)
				if os.path.isdir(tmpitem):
					shutil.copytree(tmpitem, os.path.join(output_dir, item))
				else:
					try:
						shutil.copy2(tmpitem, output_dir)
					except Exception as e:
						logging.warning('Unable to copy files : %s' % (str(e)))
	except Exception as e:
		logging.warning('Unable to copy files reccursivly : %s' % (str(e)))
