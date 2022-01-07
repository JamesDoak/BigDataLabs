#!/usr/bin/env python

import sys

# get all lines from stdin 
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	
	# split the line into words/keys
	keys = line.split()
	
	# output tuples (key, 1) in tab-delimited format
	for key in keys:
		value = 1
		print( "%s\t%d" % (key, value) )
		
