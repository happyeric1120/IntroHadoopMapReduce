#!/usr/bin/python

# For this mapper function, it just simply print out the line.
# Because some incomplete data rows also contains the words fantastic and fantastically

import sys
import csv

def mapper():
    #reader = csv.reader(sys.stdin, delimiter='\t')
    
    #next(reader, None)

    for line in sys.stdin:
        #if len(line) == 19:
        #Id, title, tagsnames, body = line[0], line[1], line[2], line[4]
        #print "{0}\t{1}\t{2}".format(Id, title, body)
	print line

if __name__ == "__main__":
    mapper()

