#!/usr/bin/python
"""
The question can be viewed as summarizations pattern.
It returns the max times of hours that a author added posts on the forum
"""

import sys

def reducer():
    # Initialize old_question_id, question_length and answer_length_list
    old_question_id = None
    question_length = 0
    answer_length_list = []

    for line in sys.stdin:
        data_mapped = line.split("\t")
        if len(data_mapped) == 3:
	    question_id, node_type, word_length = data_mapped

	    # convert word_length from string to int
	    word_length = int(word_length)
	    # Clean node_type
	    node_type = node_type.strip()


	    if old_question_id and old_question_id != question_id:
		# The question_id is the new one, so print the previous question first
		print "{0}\t{1}\t{2}".format(old_question_id, question_length, calculateAverWord(answer_length_list))

		# Replace the old question with the new question
		# Initialize all the variables
		old_question_id = question_id
		question_length = 0
		answer_length_list = []


	    # If the question_id is the same with the old_question_id
	    # Determine the node_type and added the word_length to either question_length or answer_length_list
	    old_question_id = question_id
	    if node_type == "question":
		# When the node_type is question, simply indicate the question_length
		question_length = word_length
	    else:
		# When the node_type is answer, add the word_length into the list
		answer_length_list.append(word_length)
	    

    # Remember to print the final author data
    print "{0}\t{1}\t{2}".format(old_question_id, question_length, calculateAverWord(answer_length_list))
    
def calculateAverWord(answer_length_list):
    if len(answer_length_list) == 0:
	# If there is no answer for that question, simply return 0
	return 0
    else:
	return float(sum(answer_length_list))/len(answer_length_list)


if __name__ == "__main__":
    reducer()
