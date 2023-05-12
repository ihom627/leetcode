#!/usr/bin/env python

#this is a leet code problem

#given two integer arrays nums1 and nums2, return an array of their intersection.
#each element in the result must appear as many times as it shows in both arrays and you 
#may return the result in any order


#approach
#put the integer arrays into dictionaries, and then walk each of the dictionaries to find the intersection

def intersection_of_two_arrays(nums1, nums2):
	print "this is nums1 = ", nums1; 
	print "this is nums2 = ", nums2; 

	dictionary1 = {};
	dictionary2 = {};

	for iter in nums1:
		if iter in dictionary1:
			dictionary1[iter] += 1;
		else:
			dictionary1[iter] = 1;

	for iter in nums2:
		if iter in dictionary2:
			dictionary2[iter] += 1;
		else:
			dictionary2[iter] = 1;

	print "this is dictionary1 = ", dictionary1;
	print "this is dictionary2 = ", dictionary2;

	intersection_result = [];

	#iterate through dictionaries
	for key in dictionary1:
		if key in dictionary2:
			intersection_result.append(key);

	print "this is intersection_result inside function ", intersection_result;		
	return(intersection_result);


def main():

	result = intersection_of_two_arrays([1, 2, 2, 1], [2, 2]);
	print "this is final returned intersection_result ", result;


	result = intersection_of_two_arrays([4, 9, 5], [9, 4, 9, 8, 4]);
	print "this is final returned intersection_result ", result;



if __name__ == "__main__":
        main()



