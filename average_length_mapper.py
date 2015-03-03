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
	    # Determine whether this one is question or answer
	    body, node_type = line[4], line[5]
	    
	    if node_type.lower() == "question":
		question_id = line[0]
		print "{0}\t{1}\t{2}".format(question_id, node_type, len(body))
	    elif node_type.lower() == "answer":
		# if the node_type is answer, question_id should be the abs_parent		
		question_id = line[7]
		print "{0}\t{1}\t{2}".format(question_id, node_type, len(body))
	    else:
		# Others such as comments, just pass.
		pass        


if __name__ == "__main__":
    mapper()
        
