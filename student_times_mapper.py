#!/usr/bin/python

import sys
import csv
import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    # Skip the first line, which is the header
    next(reader, None)
    # Define the time format
    fmt = "%Y-%m-%d %H:%M:%S.%f"

    for line in reader:
	# if this is a complete data point which contains 19 columns        
	if len(line) == 19:
	    author_id, added_time = line[3], line[8]
	    # Remove the time zone information
	    added_time = added_time[:-3]
	    # Convert time string to datetime object
	    added_time = datetime.datetime.strptime(added_time, fmt)
	    print "{0}\t{1}".format(author_id, added_time.hour)
    
        

if __name__ == "__main__":
    mapper()
        
