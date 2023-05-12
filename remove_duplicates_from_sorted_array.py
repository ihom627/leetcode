#!/usr/bin/env python
#this is a leet code problem

#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
#such that each unique element appears only once. The relative order of the elements should 
#be kept the same. Then return the number of unique elements in nums.

def remove_duplicates(list_of_ints):

	dict_of_ints = {};
	for i in range(0, len(list_of_ints)):
		print "integer = ", list_of_ints[i]; 
		dict_of_ints[list_of_ints[i]] = 1

	print dict_of_ints.keys()



def main():
        remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5])



if __name__ == "__main__":
        main()


