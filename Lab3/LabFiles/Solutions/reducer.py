#!/usr/bin/env python

import sys

last_key = None
running_total = 0

# input comes from stdin 
for input_line in sys.stdin:
	# remove leading and trailing whitespace
	input_line = input_line.strip()
	
	# parse the input we got from mapper.py
	this_key, value = input_line.split("\t", 1)
	# convert value (currently a string) to int
	value = int(value)
	
	if last_key == this_key:
		running_total += value
	else:
		if last_key:
			print( "%s\t%d" % (last_key, running_total) )
		running_total = value
		last_key = this_key

if last_key == this_key:
	print( "%s\t%d" % (last_key, running_total) )


