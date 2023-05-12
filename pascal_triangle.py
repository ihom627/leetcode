#!/usr/bin/env python
#this is a leet code problem

#print out Pascal's triangle


#approach 
#use for loops


def pascal_triangle(num):

	list1 = []; #an empty list  

	for i in range(num): # row loops
		list1.append([]);  
		list1[i].append(1); 

		for j in range(1, i): # column loops 
			list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j]);  

		if (num != 0 and i != 0):  
			list1[i].append(1);


	print(list1);


def main():
	pascal_triangle(5);


if __name__ == "__main__":
        main()






