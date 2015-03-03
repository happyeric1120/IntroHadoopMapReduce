#!/usr/bin/python
"""
The question can be viewed as summarizations pattern.
It returns the max times of hours that a author added posts on the forum
"""

import sys

def reducer():
    # Initialize old_author_id and hour_list
    old_author_id = None
    hour_list = initNewHourList()
    for line in sys.stdin:
        data_mapped = line.split("\t")
        if len(data_mapped) == 2:
	    author_id, added_hour = data_mapped
	    # Convert the hour into int, so it can be used as list index
	    added_hour = int(added_hour)

	    if old_author_id and old_author_id != author_id:
		# The author_id is the new one, so print the previous author
		printAuthorMaxHourList(old_author_id, hour_list)
		# Replace the old author with the new author
		# Initialize the hour list
		old_author_id = author_id
		hour_list = initNewHourList()

	    # If the author_id is the same with the old_author_id
	    # Simple added the post hour into the hour list
	    old_author_id = author_id
	    hour_list[added_hour] +=1

    # Remember to print the final author data
    printAuthorMaxHourList(old_author_id, hour_list)

def initNewHourList():
    # This function creates a list with 24 zeros elements
    # Each index indicates the hour, and the elements indicates the number of hour
    return [0]*24

def findMaxHourFromHourList(hour_list):
    # This function takes the hour_list from a single author
    # Calculate the max number of the hour that the author added posts
    # Find the tie hour and return as a list
    max_value_hour = max(hour_list)
    max_hour_list = []
    for i in range(len(hour_list)):
	if hour_list[i] == max_value_hour:
	    max_hour_list.append(i)
    return max_hour_list

def printAuthorMaxHourList(old_author_id, hour_list):
    # This functions simple print the author id and the hour with the most post
    max_hour_list = findMaxHourFromHourList(hour_list)
    for i in max_hour_list:
        print old_author_id,"\t",i


if __name__ == "__main__":
    reducer()
