"""
Trees: Unlike Arrays, Linked Lists, Stack and queues, which are linear data structures, trees are hierarchical
data structures.

Tree Vocabulary: The topmost node is called root of the tree. The elements that are directly under an element
are called its children. The element directly above something is called its parent. For example,
‘a’ is a child of ‘f’, and ‘f’ is the parent of ‘a’. Finally, elements with no children are called leaves.

                          tree
                          ----
                           j    <-- root
                         /   \
                        f      k
                      /   \      \
                     a     h      z    <-- leaves

"""

# A class that represents an individual node in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# create root
root = Node(1)

''' 
following is the tree after above statement 
    		 1 
	       /   \ 
	    None   None
'''

root.left = Node(2)
root.right = Node(3)

''' 
2 and 3 become left and right children of 1 
    		  1 
	      /      \ 
		 2	       3 
	    / \      /   \ 
    None  None  None  None
'''

root.left.left = Node(4)
'''
4 becomes left child of 2 
            		 1 
                /    	  \ 
             2       		 3 
	     /      \	     /      \ 
       4       None    None     None 
    /    \ 
  None   None 
'''

