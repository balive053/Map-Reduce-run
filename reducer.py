#! /usr/bin/env python3

#Import required libraries
import sys

# Initialize empty variables needed to store later values
current_date = None
total_temp = 0
temp = 0
date = ''
counter = 0
mean = 0
temp_list = []


## Helper code
# function to find median
def find_median():
	# sort the list from smallest to largest
	temp_list.sort()
	# find the index of the mid-point of the list
	mid_point = len(temp_list) // 2
	# find median value from mid-point index
	median = (temp_list[mid_point] + temp_list[~mid_point]) / 2
	return median

# function to find variance	
def find_variance():
	# calculate the average of the temperature list
	ave = sum(temp_list) / len(temp_list)
	# calculate the variance
	var = sum((x - ave)**2 for x in temp_list) / len(temp_list)
	return round(var, 1)
	
# function to min value:
def find_min():
	# sort the list from smallest to largest
	temp_list.sort()
	# set min as first value in list
	min = temp_list[0]
	return min
	
# function to max value:
def find_max():
	# sort the list from smallest to largest
	temp_list.sort()
	# set max as last value in list
	max = temp_list[-1]
	return max

# Print list of headers
print ("%s\t\t%s\t%s\t%s\t%s\t%s" % ('date', 'mean', 'median',  
					'min', 'max', 'var'))

for line in sys.stdin:
	(date, temp) = line.split('\t')
	temp = int(temp)
	# Itterations for if the date matches the current date (previous line)
	if date == current_date:
		# Total temp and counter for mean calculation
		total_temp += temp
		counter += 1
		# Calculate Mean
		mean = round(total_temp/counter, 1)
		# Add temp to list for median
		temp_list.append(temp)
		
		
	# Iterations for if it is the first time encountering the date (new date)	
	else:
		# If current date already exists, calculate 
		if current_date:
			# Calculate Mean
			mean = round(total_temp/counter, 1)
			# Print values
			print ("%s\t%s\t%s\t%s\t%s\t%s" % (current_date, mean, find_median(), 
					find_min(), find_max(), find_variance()))
			
		# Reset for next date
		total_temp = temp
		current_date = date
		counter = 1
		temp_list = []
		

		# Add temp to list for median
		temp_list.append(temp)

# To cover final iteration
if date == current_date:
	# Print values
	print ("%s\t%s\t%s\t%s\t%s\t%s" % (current_date, mean, find_median(), 
					min(temp_list), max(temp_list), find_variance()))