#!/usr/bin/env python
#this is a leet code problem

#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
#or -1 if needle is not part of haystack.

def first_occurence(source, target):

	found = 0;
	print "this is the source = ", source
	print "this is the target = ", target 
	for i in range(0, len(target)):
		print "this is the target slice = ", target[i: i + len(source)]	
		if (source == target[i: i + len(source)]):
			print "FOUND source in target at index i = ", i			
			return(i);
	return(-1);
		


def main():
        result = first_occurence("sad", "sadbutsad")



if __name__ == "__main__":
        main()


