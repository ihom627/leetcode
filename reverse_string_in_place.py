#!/usr/bin/env python

#this is a leet code problem

#given an array or characters, reverse the array in place


#approach
#move pointers from the left and right and swap contents

def reverse_string_in_place(string):
	print "this is string = ", string; 

	left, right = 0, len(string)-1;

	while (left < right):
		temp = string[right];
		string[right] = string[left];
		string[left] = temp;
		left += 1;
		right -= 1;

	return(string);


def main():
	reverse_string = reverse_string_in_place(["h", "e", "l", "l", "o"]);
	print "the reverse_string =", reverse_string;

	reverse_string = reverse_string_in_place(["H", "a", "n", "n", "a", "h"]);
	print "the reverse_string =", reverse_string;


if __name__ == "__main__":
        main()



