#!/usr/bin/env python
#this is a leet code problem

#given an integer array nums, return True if any value appears atleast twice in the array and return false
#if every element is distinct


#approach 
#put the array elements into a dictionary, where the key is the number and the value is the count
#then print out the values of the dictionary


def contains_duplicate(nums):
        print "this is array of integers nums = ", nums;

	number_dictionary = {};

	for iter in nums:
		if iter in number_dictionary:
			number_dictionary[iter] += 1;
		else:
			number_dictionary[iter] = 1;

	print "number_dictionary = ", number_dictionary;

	#iterate over values
	distinct = 1;
	for key in number_dictionary:
		if number_dictionary[key] == 2:
			return(True);
		elif number_dictionary[key] != 1:
			distinct = 0;

	if distinct == 1:
		return(False);	


def main():
	result = contains_duplicate([1, 2, 3, 1]);
	print "this is the result = ", result;

	result = contains_duplicate([1, 2, 3, 4]);
	print "this is the result = ", result;

	result = contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]);
	print "this is the result = ", result;



if __name__ == "__main__":
        main()






