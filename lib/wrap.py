#-*- coding: utf8 -*-

"""
Get a part of the content. Limit to:
	- the first blank line
	- *limit* number or words
"""
def wrap(content, limit=150):
	lines = content.split("\n")
	ret = []

	l = 0
	for line in lines:
		# Split at the first blank line
		if len(line.strip()) == 0:
			break
		else:
			l += len(line.split())
			ret.append(line)

		if l >= limit:
			break

	ret[len(ret) - 1] += '...'

	return '\n'.join(ret)
