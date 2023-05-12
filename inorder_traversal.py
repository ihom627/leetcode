#!/usr/bin/env python
#this is a leet code problem

#perform inorder traversal of a b-tree


#approach is to use recursion
#at each node peform Go Left, Visit, Go Right

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def inorder_traversal(self, root):

	#terminal condition
	if self is None:
		return;

	inorder_traversal(self.left):
	print "this is node value = ", self.value;
	inrder_traversal(self.right):


def main():
	inorder_traversal();


if __name__ == "__main__":
        main()






