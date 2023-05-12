#!/usr/bin/env python
#this is a leet code problem

#count the nummber of 1s in a 32 bit unsigned integer 


#approach 
#apply a bit mask 1 AND with input to get right most bit
#work from the right to left  


def hamming_count(orig_unsigned_integer):
        print "this is orig_unsigned_integer = ", orig_unsigned_integer;
	result = 0;

	for i in range(32):
		bit = (orig_unsigned_integer >> i) & 1; #logical AND input bit
		if bit == 1:
			result += 1;
	
	print "this is hamming count result = ", result;
 
	return(result);


def main():
	result = hamming_count(1);
	print "this is the result of the hamming count = ", result;

	result = hamming_count(5);
	print "this is the result of the hamming count = ", result;

	result = hamming_count(43261596);
	print "this is the result of the hamming_count = ", result;

	result = hamming_count(4294967293);
	print "this is the result of the hamming_count = ", result;

if __name__ == "__main__":
        main()






