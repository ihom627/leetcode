#!/usr/bin/env python

#this is a leet code problem

#given an integer n, return True if it is a power of three.  Otherwise return false
#if there exists an integer such that n == 3**n


#approach
#brute force approach by calculating the third power until reaches the number

def power_of_three(num):
	print "this is num = ", num; 

	if num <= 0:
		return(False, -1);


	#iterate through integers 
	for i in range(1, num):
		if i*i*i == num:
			return(True, i);
	return(False, -1); 


def main():
	result, integer = power_of_three(27);
	print "the result is ", result;
	print "this is power of three integer = ", integer; 

	result, integer = power_of_three(0);
	print "the result is ", result;
	print "this is power of three integer = ", integer;

        result, integer = power_of_three(-1);
	print "the result is ", result;
	print "this is power of three integer = ", integer;


if __name__ == "__main__":
        main()



