#!/usr/bin/env python
#this is a leet code problem

roman_to_integer_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}

def roman_to_integer(roman_list):
	total = 0;
        for i in range(0, len(roman_list)):
		print "this is current roman index value = ", roman_list[i];
		print "this is current integer index value = ", roman_to_integer_dict.get(roman_list[i]);
		total = total + roman_to_integer_dict.get(roman_list[i]);
	print "this is the total = ", total;
	return(total);


def main():
        roman_to_integer("IV")
        roman_to_integer("LIV")
        roman_to_integer("CV")



if __name__ == "__main__":
        main()


