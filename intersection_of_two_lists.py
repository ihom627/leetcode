#!/usr/bin/env python
#this is a leet code problem

#given two lists, the find the intersecting node if there is one


#approach 
#put the elements of the first list into a dictionary, and then walk the second list and find the
#first entry already in the dictionary


def intersection_of_two_lists(list1, list2):
        print "this is list1 ", list1;
        print "this is list2 ", list2;

	node_dictionary = {};

	for iter1 in list1:
		if iter1 in node_dictionary:
			node_dictionary[iter1] += 1;
		else:
			node_dictionary[iter1] = 0;	

	for iter2 in list2:
		if iter2 in node_dictionary:
			return(iter2);
	return(-1);

def main():
	result = intersection_of_two_lists([1, 2, 4, 6, 7], [8, 9, 4, 6, 7]);
	print "this is the result of the intersection of two lists", result;


if __name__ == "__main__":
        main()






