#!/usr/bin/env python
#this is a leet code problem

#reverse the bits of a given 32 bit unsigned integer 


#approach 
#apply a bit mask 1 AND with input to get right most bit
#work from the right to left  
#the result needs to be written back using the OR with the result starting from the left
#work from the left to the right


def reverse_bits(orig_unsigned_integer):
        print "this is orig_unsigned_integer = ", orig_unsigned_integer;
	result = 0;

	for i in range(32):
		bit = (orig_unsigned_integer >> i) & 1; #logical AND input bit
		result = result | (bit << (31 -i)) #logical OR result bit
	
	print "this is reversed result = ", result;
 
	return(result);


def main():
	result = reverse_bits(1);
	print "this is the result of the reverse_bits = ", result;

	result = reverse_bits(43261596);
	print "this is the result of the reverse_bits = ", result;

	result = reverse_bits(4294967293);
	print "this is the result of the reverse_bits = ", result;

if __name__ == "__main__":
        main()






