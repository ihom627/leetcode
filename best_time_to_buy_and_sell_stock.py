#!/usr/bin/env python
#this is a leet code problem

#you are given an array prices where prices[i] is the price of a given stock on the ith day
#you want to maximize your profit by choosing a single day to buy one stocka and a different day 
#in the future to sell that stock
#return the maximum profit


#approach 
#find the smallest and largest numbers
#check smallest has an index before the largest
#greedy solution is to have two for loops to iterate over the list and check if the profit is maximized


def buy_sell_stock(prices):
	buy = 0;
	max_profit = 0;

	for i in range(0, len(prices)):
		for j in range(i, len(prices)):
			if (prices[j] - prices[i]) > max_profit:
				buy = prices[i];
				max_profit = prices[j] - prices[i];	

	print "this is buy = ", buy;
	print "this is max_profit = ", max_profit;
	

def main():
	buy_sell_stock([7, 1, 5, 3, 6, 4]);
	buy_sell_stock([7, 6, 5, 4, 3, 2, 1]);


if __name__ == "__main__":
        main()






