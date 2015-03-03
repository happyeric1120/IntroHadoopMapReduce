#!/usr/bin/python

# So in the reducer function, it only collect all the ID and sort it.

import sys
import re

def reducer():
    word_list_fantastic = []
    for line in sys.stdin:
	data_mapped = line.split("\t")
	if len(data_mapped) == 2:
	    Id = int(data_mapped[1].strip("\n"))
	    word_list_fantastic.append(Id)
    word_list_fantastic.sort()
    print "{0}\t{1}".format("fantastic list", word_list_fantastic)


if __name__ == "__main__":
    reducer()

        
