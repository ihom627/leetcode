#!/usr/bin/env python
#this is a leet code problem

#You are given a large integer represented as an integer array digits, where each digits[i] is the ith
#digits of the integer.  The digits are ordered from the most significant to least significant in the
#left to right order.  The large integer does not contain any leading 0s

#Increment the large integer by one and return the resulting array of digits 

#approach: 
#convert the list to an integer
#add one
#convert the integer back to a list 

def plus_one(digits):
	print "this is digits = ", digits;	

	number = 0;
	for current_digit in digits:
		number = number * 10 + current_digit
	print "this is the integer =", number;  

	number_plus_one = number + 1
	print "this is the integer plus one = ", number_plus_one;

	result = [];
	while number_plus_one > 0:
    		number_plus_one, remainder = divmod(number_plus_one, 10)
    		result.insert(0, remainder)

	print "this is the resulting list", result;


def main():
        plus_one([1, 2, 3])
        plus_one([4, 3, 2, 1])
        plus_one([9])



if __name__ == "__main__":
        main()






