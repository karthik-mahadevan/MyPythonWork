import math
import locale


locale.setlocale(locale.LC_ALL, 'en_US')

while (1):
	for i in range(1,10000001):
		print locale.format("%d", i, grouping=True)
	break