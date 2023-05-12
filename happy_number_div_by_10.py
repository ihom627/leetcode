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

		sum_squares = 0;
		while result:
			digit = result % 10;
			print "this is the digit under test = ", digit;	
			sum_squares = sum_squares + (digit)**2;
			result = result / 10;
			print "this is iteration result = ", result;

		if (sum_squares == 1):
			return(True);
		result = sum_squares;
		max_iterations -= 1;
 
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






