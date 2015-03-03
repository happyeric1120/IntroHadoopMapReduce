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
	    # Get the tagsname and node_type from line
	    tagsname, node_type = line[2], line[5]
	    
	    # Two approaches to classify tagsname for question, answer or comments
	    # It can either select the specific node_type from mapper here or
	    # select in the reducer, but here I just print the tagsname and node_type
	    
	    # The tag is separate by blank
	    tag_list = tagsname.split(" ")

	    for tag in tag_list:
		print "{0}\t{1}".format(tag, node_type)   


if __name__ == "__main__":
    mapper()
        
