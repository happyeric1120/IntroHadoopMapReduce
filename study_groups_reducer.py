#!/usr/bin/python
"""
The question can be viewed as summarizations pattern.
It returns the max times of hours that a author added posts on the forum
"""

import sys

def reducer():
    # Initialize old_question_id, question_length and answer_length_list
    old_question_id = None
    author_id_list = []

    for line in sys.stdin:
        data_mapped = line.split("\t")
        if len(data_mapped) == 3:
	    question_id, author_id, node_type = data_mapped

	    # Looks like the format of the answer converts author_id to number
	    author_id = int(author_id)
	    # Clean node_type
	    node_type = node_type.strip()


	    if old_question_id and old_question_id != question_id:
		# The question_id is the new one, so print the previous question first
		print "{0}\t{1}".format(old_question_id, author_id_list)

		# Replace the old question with the new question
		# Initialize all the variables
		old_question_id = question_id
		author_id_list = []

	    # If the question_id is the same with the old_question_id
	    # Determine the node_type to insert or append the author_id
	    old_question_id = question_id
	    if node_type == "question":
		# When the node_type is question, insert the id to the first position, 
		# so we can tell who ask this question
		author_id_list.insert(0, author_id)
	    else:
		# When the node_type is answer, append the author
		author_id_list.append(author_id)
	    

    # Remember to print the final author data
    print "{0}\t{1}".format(old_question_id, author_id_list)
    


if __name__ == "__main__":
    reducer()
