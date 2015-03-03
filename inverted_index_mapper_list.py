#!/usr/bin/python

# This is another version to do the inverted index
# Instead of print out the entities of the body, it will only print the Id for
# the specific post, so it can decrease the size of file transferring to reducer
# So in the reducer function, it only collect all the ID and sort it.

# However, in order to successfully get the ID, some incomplete data points have 
# been eliminated by len(line) == 19
# Since some fantastic or fantastically words appear in some incomplete data rows.

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    
    next(reader, None)

    for line in reader:
        if len(line) == 19:
            Id, title, body = line[0], line[1], line[4]
	    
            if len(re.findall("fantastic", title)) != 0 and len(re.findall("fantastically",title)) == 0: 
                for i in range(len(re.findall("fantastic", title))):
		    print "{0}\t{1}".format("fantastic", Id)
	    

            if len(re.findall("fantastic", body)) != 0 and len(re.findall("fantastically",body)) == 0: 
                for i in range(len(re.findall("fantastic", body))):
		    print "{0}\t{1}".format("fantastic", Id)
	

if __name__ == "__main__":
    mapper()

