#!/usr/bin/env python
#this is a leet code problem

#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

def longest_common_prefix(list_of_strings):
	keep_looping = 1;
	while (list_of_strings and keep_looping):
		prefix = "";
		word = list_of_strings.pop();	
		print "this is the word under test = ", word;
		for i in range(0, len(word)):
			old_prefix = prefix;
			prefix = prefix + word[i];
			print "prefix of word = ", prefix;	

	        	for index in range(0, len(list_of_strings)):
				print "iter_word = ", list_of_strings[index]; 
				if prefix in list_of_strings[index]:
					print "FOUND prefix ", prefix, " in ", list_of_strings[index] 
				else:
					print "NOT found prefix ", prefix, " in ", list_of_strings[index]
					keep_looping = 0;
					break;
			if (keep_looping == 0):
				break;
	print "this is returned old_prefix ", old_prefix;

def main():
        longest_common_prefix(["flower", "flow", "flight"])
        longest_common_prefix(["acorn", "arrow", "around", "alcove"])
        longest_common_prefix(["garbage", "flow", "flight"])



if __name__ == "__main__":
        main()


