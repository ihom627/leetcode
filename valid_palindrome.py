#!/usr/bin/env python
#this is a leet code problem

#a phrase is a palindrome if after converting all uppercase letters into lowercase letters and removing
#all non-alphanumeric characters, it reads the same forward and backward.  Alphanumeric characters include
#letters and numbers


#approach 
#walk in from both ends and constantly match characters or numbers and skipping everything else


def valid_palindrome(orig_string):
        print "this is orig string ", orig_string;

	left = 0
	right = len(orig_string) -1;

	while (left < right): #they don't meet

		while left < right and not (orig_string[left].isalnum()): 
			left+=1;
		left_temp = orig_string[left].lower();

                while left < right and not (orig_string[right].isalnum()): 
			right-=1;
		right_temp = orig_string[right].lower();

		if left_temp != right_temp:
			return(False);
		else:
			left += 1;
			right -= 1;

	return(True);
	

def main():
	result = valid_palindrome("A man, a plan a canal: Panama");
	print "this is the result of the palindrome test", result;


if __name__ == "__main__":
        main()






