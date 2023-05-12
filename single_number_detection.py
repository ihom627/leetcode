#!/usr/bin/env python
#this is a leet code problem

#given an array of integers nums, every element appears twice except for onem, find that single number
#must implement a solution with linear runtime complexity and use only constant extra space


#approach 
#put the array elements into a dictionary, where the key is the number and the value is the count
#then print out the values of the dictionary


def single_number_detection_using_dictionary(nums):
        print "this is array of integers nums = ", nums;

	number_dictionary = {};

	for iter in nums:

		if iter in number_dictionary:
			number_dictionary[iter] += 1;
		else:
			number_dictionary[iter] = 1;

	print "number_dictionary = ", number_dictionary;


def single_number_detection_using_exor(nums):
	print "this is arry of integers nums = ", nums;

	result = 0;

	for iter in nums:
		result ^= iter;
	
	print "this is single number = ", result;
	

def main():
	single_number_detection_using_dictionary([1, 1, 3, 3, 4]);
	single_number_detection_using_exor([1, 1, 3, 3, 4]);


if __name__ == "__main__":
        main()






