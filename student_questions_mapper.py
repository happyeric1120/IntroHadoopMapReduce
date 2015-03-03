#!/usr/bin/python

import sys
import csv
import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    # Skip the first line, which is the header
    next(reader, None)

    for line in reader:
	# if this is a complete data point which contains 19 columns        
	if len(line) == 19:
	    # Get the author_id and node_type
	    author_id, node_type = line[3], line[5]
	    if node_type == "question" or node_type == "answer":
	        print "{0}\t{1}".format(author_id, node_type)
	    

if __name__ == "__main__":
    mapper()
        
