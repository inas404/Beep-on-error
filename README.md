# Beep-on-exception
This is a simple python template I made to beep on exception and print it out. I needed it mostly when i run a code that might take so long running in the background and it suddenly stops on error and i don't notice till the end. This is justo to alert me.

All you need to do is to import these packages:

```python
import os
import traceback
import logging
```

Then put your code in a try-exception block:
```python
try:

"""

writ your code here.

"""
except Exception as e:
	logging.error(traceback.format_exc())
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1, 1000)) 
	# 1 is duration per second and 1000 is frequency per hertz
```
