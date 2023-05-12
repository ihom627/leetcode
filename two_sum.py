#!/usr/bin/env python
#this is a leet code problem


def two_sum(list_nums, target_num):
	print "this is list_nums = ", list_nums , "target_num = ", target_num;	

	outer_index = 0
	for outer_index in range(0, len(list_nums)):
		outer_index_value = list_nums[outer_index]
		print "outer_index_value = ", outer_index_value;	
		for inner_index in range(outer_index + 1, len(list_nums)):
			inner_index_value = list_nums[inner_index];
			print "inner_index_value = ", inner_index_value;

			total = outer_index_value + inner_index_value;
			print "this is total = ", total; 		

                	if total == target_num:
				print "FOUND match, returning indices ", outer_index, inner_index 




def main():
        two_sum([2, 7, 11, 15], 9)
        two_sum([2, 7, 11, 15, 1, 3, 5], 16)
        two_sum([2, 7, 11, 15, 1, 3, 5], 8)
        two_sum([2, 7, 11, 15, 1, 3, 5], 18)



if __name__ == "__main__":
        main()






