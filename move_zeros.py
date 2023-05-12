#!/usr/bin/env python

#this is a leet code problem

#given an array nums containing, move the 0s to the end while maintaining the relative order of the non-zeros 
#must do this in-place without making a copy of the array

#approach
#do a bubble sort to move the 0s to the far right of the array

def move_zeros(nums):
	print "this is nums = ", nums; 

	#iterate through nums 
	for i in range(0, len(nums)):
		for j in range(i, len(nums)):
			if nums[i] == 0:
				temp = nums[j];
				nums[j] = nums[i];
				nums[i] = temp;
	return(nums)


def main():
	moved_nums = move_zeros([3, 0, 1]);
	print "this is moved zeros in moved_nums", moved_nums; 

	moved_nums = move_zeros([0, 1, 0, 3, 12]);
	print "this is moved zeros in moved_nums", moved_nums;


if __name__ == "__main__":
        main()



