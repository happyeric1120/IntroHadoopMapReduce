#!/usr/bin/python

# In the reducer function, it just get the line and check whether the key words are inside.
# For some reasons, one line data containing "fantastically" is incomplete, so I can not find the ID for it.

import sys
import re

def reducer():
    word_ctr_fantastic = 0
    word_list_fantastically = []
    word_ctr_fantastically = 0
    for line in sys.stdin:

	line = line.lower()
        if len(re.findall("fantastic", line)) != 0:
            word_ctr_fantastic += len(re.findall("fantastic", line))    

        if len(re.findall("fantastically", line)) != 0:
	    word_ctr_fantastically += len(re.findall("fantastically", line))
	    print line
	    data_mapped = line.split("\t")
	    for i in range(len(re.findall("fantastically", line))):
		if len(data_mapped[0]) < 30:
		    word_list_fantastically.append(data_mapped[0])


    print "word fantastic = ", word_ctr_fantastic
    print "word fantastically = ", word_ctr_fantastically
    print "word fantastically list = ", word_list_fantastically

if __name__ == "__main__":
    reducer()

        
