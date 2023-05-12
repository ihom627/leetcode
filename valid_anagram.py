#!/usr/bin/env python

#this is a leet code problem

#given two strings, return True if they are anagrams, otherwise return False

#approach
#put each of the strings into a dictionary, then compare the dictionaries if they are anagrams

def valid_anagram(string1, string2):
	print "this is string1 = ", string1; 
	print "this is string2 = ", string2; 

	dictionary1 = {};
	dictionary2 = {};

  
	#iterate through string1
	for i in range(0, len(string1)):
		if string1[i] in dictionary1:
			dictionary1[string1[i]] += 1;
		else:
			dictionary1[string1[i]] = 1;

	print "this is dictionary1 = ", dictionary1;

	#iterate through string2
	for i in range(0, len(string2)):
		if string2[i] in dictionary2:
			dictionary2[string2[i]] += 1;
		else:
			dictionary2[string2[i]] = 1;

	print "this is dictionary2 = ", dictionary2;

	if dictionary1 == dictionary2:
		return(True);
	else:
		return(False);



def main():
	result = valid_anagram("anagram", "nagaram");
	print "valid_anagram is ", result; 

	result = valid_anagram("rat", "car");
	print "valid_anagram is ", result;


if __name__ == "__main__":
        main()



