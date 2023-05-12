#!/usr/bin/env python
#this is a leet code problem

#given a list, find the element that exists the majority number of times 


#approach 
#put the elements of the list into a dictionary where the value is the count, then print out the values
# and see which one occurs a majority number of times


def majority_element(list1):
        print "this is list1 ", list1;

	node_dictionary = {};

	for iter1 in list1:
		if iter1 in node_dictionary:
			node_dictionary[iter1] += 1;
		else:
			node_dictionary[iter1] = 1;	

	for key in node_dictionary:
		if node_dictionary[key] > len(list1)/2:
			return(key);
	return(-1);



def main():
	result = majority_element([2, 2, 1, 1, 1, 2, 2]);
	print "this is the result of the majority element", result;


if __name__ == "__main__":
        main()






