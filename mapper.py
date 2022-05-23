#! /usr/bin/env python3


import sys

# Iterate through rows 
for line in sys.stdin:
	# Splitting values based on "," demiliter and assign values
	val = line.strip().split(",")
	(date, temp) = (val[1], val[8])
	
	# Only take rows where a temperature is present and print output
	if temp.lstrip("-").isdigit(): 
		print ("%s\t%s" % (date, temp))
	
