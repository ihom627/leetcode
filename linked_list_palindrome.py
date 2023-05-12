#!/usr/bin/env python
#this is a leet code problem

#determine if a linked list is a palindrome or not


#approach 
#reverse the linked list and see if it matches the original

# Definition for a linked list node.
class Node:
	
	# constructor
	def __init__(self, data):
		self.data = data 
		self.next = None;

#create a linked list class with a head node
class LinkedList:
	
	# function to initialize head
	def __init__(self):
		self.head = None;

	#insert into a linked list in ascending order
	def insert(self, data):

		#create new node
		newNode = Node(data);
		print "creating new Node = ", newNode.data;

		#empty linked list
		if self.head is None:
			self.head = newNode;	
			print "head is empty so creating it";

		#special case that new data is less than head 
		elif self.head.data >= newNode.data:
			newNode.next = self.head
			self.head = newNode;
			print "new node is less than head, so put new node in head position";

		else:
			current = self.head;
			print "starting at the head with value ", current.data;
			while (current.next is not None and current.next.data <= newNode.data): #if current < new 
				current = current.next; #keep traversing
				print "keep going in LL";

			#found place to insert
			newNode.next = current.next;
			current.next = newNode;
			print "found position to insert node into LL";

	#print a linked list
	def printLL(self):
		current = self.head;

		print "printing out the linked_list"; 
		while(current):
			print(current.data);
			current = current.next;


	#reverse a linked list
	def reverse_linked_list(self):
		prev, current, next = None, self.head, None;
		
		while (current):
			next = current.next;
			current.next = prev;
			prev = current;
			current = next;

		self.head = prev;	

	#palindrome check
	def palindrome_check(self):
		current = self.head;
		
		stack = [];

		#push contents of linked list onto a stack
		while(current):
			stack.append(current.data);
			current = current.next;
		
		print "this is contents of stack ", stack;

		#reverse the stack contents
		stack.reverse();

		print "this is contents of reversed stack ", stack;

		current = self.head;
		while (stack and current):
			if stack.pop() != current.data:
				return(False);
		return(True);	
	


def main():
	LL = LinkedList();

	#insert nodes 
	LL.insert(5);			
	LL.insert(7);			
	LL.insert(9);			
	LL.insert(1);			
	LL.insert(6);			
	LL.insert(8);			

	print "this is LL";
	LL.printLL();

	#check for palindrome
	result = LL.palindrome_check();
	print "this is palindrome_check result = ", result;

	LL2 = LinkedList();

        #insert nodes
        LL2.insert(5);
        LL2.insert(5);
        LL2.insert(5);

        print "this is LL2";
        LL2.printLL();

        #check for palindrome
        result = LL2.palindrome_check();
        print "this is palindrome_check result = ", result;

	

if __name__ == "__main__":
        main()






