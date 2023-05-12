#!/usr/bin/env python
#this is a leet code problem

#You are climbing a staircase, it takes n steps to reach the top.
#Each time you can climb either 1 or 2 steps, how many distinct ways can you climb to the top


#approach is to apply recursion
#observe that for Step 1, there is only one way
#for Step 2, there are two ways (1 + 1, or 2)
#for Step 3, either get there from Step 2 in one way, or from Step by two ways (1 + 1, or 2)
#for any Step n = (Step n - 1) + (Step n - 2)  


def climbing_steps(target_steps):
	print "this is target_steps = ", target_steps;	

	number_ways = 0;

        #terminal condition
	if (target_steps == 1):
		return 1;
	elif (target_steps == 2):
		return 2;
	#recursion
	else:
		return climbing_steps(target_steps - 1) + climbing_steps(target_steps -2);



def main():
	number_ways = climbing_steps(5);
	print "this is the number_ways = ", number_ways;


if __name__ == "__main__":
        main()






