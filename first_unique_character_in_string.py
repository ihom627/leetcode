#!/usr/bin/env python

#this is a leet code problem

#given a string, find the first non-repeating character in it and return its index. If it does not exist, return -1


#approach
#maintain two dictionaries, one for count and another for index

def first_unique_character_in_string(string):
	print "this is string = ", string; 
	
	dictionary_count = {};
	dictionary_index = {};

	for i in range(0, len(string)):
		if string[i] in dictionary_count:
			dictionary_count[string[i]] += 1;
			dictionary_index[string[i]] = i;
		else:
			dictionary_count[string[i]] = 1;
			dictionary_index[string[i]] = i;
 
	print "dictionary_count = ", dictionary_count;
	print "dictionary_index = ", dictionary_index;

	for index in range(0, len(string)):
		keys = [k for k, v in dictionary_index.items() if v == index] 
		if keys:
			key_of_lowest_index = keys[0];
			print "this is key_of_lowest_index = ", key_of_lowest_index;
			if dictionary_count[key_of_lowest_index] == 1:
				return(key_of_lowest_index, index);
	return(-1, -1);
	


def main():

	result, index = first_unique_character_in_string("leetcode");
	print "this is result and index ", result, index;

	result, index = first_unique_character_in_string("loveleetcode");
	print "this is result and index ", result, index;

        result, index = first_unique_character_in_string("aabb");
        print "this is result and index ", result, index;


if __name__ == "__main__":
        main()



