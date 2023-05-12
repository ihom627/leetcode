#!/usr/bin/env python
#this is a leet code problem

#reverse a linked list 


#approach 
#using three pointers: prev, current, next

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


def main():
	LL = LinkedList();

	#insert nodes 
	LL.insert(5);			
	LL.insert(7);			
	LL.insert(9);			
	LL.insert(1);			
	LL.insert(6);			
	LL.insert(8);			

	LL.printLL();

	LL.reverse_linked_list();

        LL.printLL();

	

if __name__ == "__main__":
        main()






