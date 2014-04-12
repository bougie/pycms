#-*- coding: utf8 -*-
import os
import shutil

def move_statics_files(static_dir, output_dir):
	if os.path.isdir(output_dir):
		shutil.rmtree(output_dir)

	if os.path.exists(static_dir):
		items = os.listdir(static_dir)
		for item in items:
			tmpitem = os.path.join(static_dir, item)
			if os.path.isdir(tmpitem):
				shutil.copytree(tmpitem, os.path.join(output_dir, item))
			else:
				shutil.copy2(tmpitem, output_dir)
