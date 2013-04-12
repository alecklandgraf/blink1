#!/usr/local/bin/python
"""
Blink1 class
"""

class Blink1(object):
	"""Blink1"""

	blink1_tool_file_path = 'lib/blink1-tool'

	def __init__(self, arg):
		super(Blink1, self).__init__()
		self.arg = arg

	def rgb(self, rgb_color):
		pass

	def blink(self, number_of_blinks, rgb_color=None):
		if rgb:
			self.rgb(rgb)

