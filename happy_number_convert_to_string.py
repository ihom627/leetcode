#!/usr/bin/env python
#this is a leet code problem

#determine if a number is happy
#replace the number with the sum of squares of its digits
#repeat the process until the final number equals 1 then it is happy 


#approach 
#work from the right to left  


def happy_number(orig_unsigned_integer):
        print "this is orig_unsigned_integer = ", orig_unsigned_integer;

	result = orig_unsigned_integer;
	max_iterations = 100;

	while (max_iterations):

		result_string = str(result);
		loop_sum = 0;
		for i in range(0, len(result_string)):
			print "this is index i = ", i;
			print "this is digit under test = ", int(result_string[i]);
			loop_sum = loop_sum + int(result_string[i]) * int(result_string[i]);
			
		print "this is the loop_sum = ", loop_sum;
		if loop_sum == 1:
			return(True);
		max_iterations -= 1;	
		result = loop_sum;
		print "this is result = ", result;
 
	return(False);


def main():
	result = happy_number(19);
	print "this is the result of the happy count = ", result;

	result = happy_number(2);
	print "this is the result of the happy count = ", result;

	"""
	result = happy_number(43261596);
	print "this is the result of the happy_count = ", result;

	result = happy_number(4294967293);
	print "this is the result of the happy_count = ", result;
	"""

if __name__ == "__main__":
        main()






