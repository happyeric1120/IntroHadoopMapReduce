#!/usr/bin/python
"""
The question can be viewed as summarizations pattern.
It returns the max times of hours that a author added posts on the forum
"""

import sys

def reducer():
    # Initialize old_question_id, question_length and answer_length_list
    old_author_id = None
    node_type_list = [0, 0]     # [question, answer]

    for line in sys.stdin:
        data_mapped = line.split("\t")
        if len(data_mapped) == 2:
	    author_id, node_type = data_mapped
	    # Clean node_type
	    node_type = node_type.strip()

	    if old_author_id and old_author_id != author_id:
		# The question_id is the new one, so print the previous question first
		print "{0}\t{1}".format(old_author_id, node_type_list)

		# Replace the old author id with the new author id
		# Initialize the node_type_list
		old_author_id = author_id
		node_type_list = [0, 0]


	    # If the question_id is the same with the old_question_id
	    # Determine the node_type and added the word_length to either question_length or answer_length_list
	    old_author_id = author_id
	    if node_type == "question":
		# When the node_type is question, simply added to first element in node_type_list
		node_type_list[0] = node_type_list[0] + 1
	    elif node_type == "answer":
		# When the node_type is answer, simply added to second element in node_type_list
		node_type_list[1] = node_type_list[1] + 1
	    

    # Remember to print the final author data
    print "{0}\t{1}".format(old_author_id, node_type_list)
    

if __name__ == "__main__":
    reducer()
