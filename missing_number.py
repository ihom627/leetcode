#!/usr/bin/env python

#this is a leet code problem

#given an array nums containing n distinct numbers in the range [0, n], return the only number
#in the range that is missing from the array

#approach
#get the length of the array as the range
#put the array into a dictionary and return the sorted keys
#then check the sorted keys are in the range

def missing_number(nums):
	print "this is nums = ", nums; 

	range_nums = len(nums); 
	print "this is range_nums = ", range_nums;

	dictionary1 = {};
  
	#iterate through nums 
	for i in nums:
		if i in dictionary1:
			dictionary1[i] += 1;
		else:
			dictionary1[i] = 1;

	for iter in range(0, range_nums + 1):
		if iter not in dictionary1:
			return(iter);

	return(-1);	



def main():
	result = missing_number([3, 0, 1]);
	print "missing_number is ", result; 

	result = missing_number([0, 1]);
	print "missing_number is ", result;

	result = missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]);
	print "missing_number is ", result;

if __name__ == "__main__":
        main()



