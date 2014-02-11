import math
i = 0
while (1):
	for i in range(1,1000001):
		comma_position =[]
		number_of_commas = math.log10(i)/3
		print "%d,%d" %(i,number_of_commas)
	break