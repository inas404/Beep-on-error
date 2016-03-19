import os
import traceback
import logging

try:
	"""
	Write your code here
	"""
	print ('Test division by zero Exception')
	print (10/0)
	
except Exception as e:
	logging.error(traceback.format_exc())
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1, 1000))
	# 1 is duration per second and 1000 is frequency per hertz