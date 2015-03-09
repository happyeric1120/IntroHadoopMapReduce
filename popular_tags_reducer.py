#!/usr/bin/python
"""
The question can be viewed as summarizations pattern.
It returns the max times of hours that a author added posts on the forum
"""

import sys

def reducer():
    # Initialize old_tag, total_tag_number, tag_list, and tag_num_list
    old_tag = None
    total_tag_number = 0
    tag_list = []
    tag_num_list = []

    for line in sys.stdin:
        data_mapped = line.split("\t")
        if len(data_mapped) == 2:
	    current_tag, node_type = data_mapped



	    if old_tag and old_tag != current_tag:
		# The current_tag is a new one, adding the old_tag and its total number into the lists
		tag_list.append(old_tag)
		tag_num_list.append(total_tag_number)

		# Replace the old_tag with the current_tag
		# Initialize the total_tag_number
		old_tag = current_tag
		total_tag_number = 0

	    # If the old_tag is the same with the current_tag
	    # Simply adding the tag total number
	    old_tag = current_tag
	    # If just need to select one certain node_type, it can make the statement here by using
	    # if node_type == "question". However, I select all node_type tags here
	    total_tag_number += 1
	    

    # Remember to add the last tag into the list and its total tag number
    tag_list.append(old_tag)
    tag_num_list.append(total_tag_number)

    # Use the selectTopList function to select the top 10 tags
    selectTopList(tag_list, tag_num_list)


def selectTopList(tag_list, tag_num_list, top = 10):
    if top > len(tag_list):
	top = len(tag_list)
    tag_top_list = []
    tag_top_num_list = []
    for i in range(top):
	# Find the max value index
	index_max = tag_num_list.index(max(tag_num_list))
	# Pop the max value tag and its value. Print it out
	print "{0}\t{1}".format(tag_list.pop(index_max), tag_num_list.pop(index_max))


    



if __name__ == "__main__":
    reducer()
