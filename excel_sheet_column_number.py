#!/usr/bin/env python
#this is a leet code problem

#given a string column_title, return the corresponding column number 


#approach 
#use ord to translate char to int and then subtract by 64
#work from the right to left and use place in the multiplier


def excel_sheet_column_number(column_title):
        print "this is column_title ", column_title;

	multiplier = 1;
	result = 0;

	#walk from the least significant to the most significant
	for index in range(len(column_title) - 1, -1, -1):
		result += (ord(column_title[index]) - 64) * multiplier;
		multiplier *= 26;
 
	return(result);


def main():
	result = excel_sheet_column_number("A");
	print "this is the result of the excel_sheet_column_number = ", result;

	result = excel_sheet_column_number("AB");
	print "this is the result of the excel_sheet_column_number = ", result;


if __name__ == "__main__":
        main()






