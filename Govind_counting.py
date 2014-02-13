import math
import locale
import time


locale.setlocale(locale.LC_ALL, 'en_US')

while (1):
	start_time = time.time()
	for i in range(1,10000001):
		print locale.format("%d", i, grouping=True)
	print "Total time :", locale.format("%d", (time.time() - start_time), grouping=True), "s"	
	break