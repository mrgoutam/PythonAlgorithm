def search(root, key):

    if root is None or root.val == key:
        return root

    # Key is greater then root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

"""
Steps:
1. Start from root
2. Compare the inserting element with root, if less than root then recurse for left,
else recurse for right.
3. If element to search is found anywhere, return true, else return false.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    mNode = Node(key)
    if root is None:
        root = mNode
    else:
        if root.val < mNode.val:
            if root.right is None:
                root.right = mNode
            else:
                insert(root.right, key)
        else:
            if root.left is None:
                root.left = mNode
            else:
                insert(root.left, key)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end=' ')
        in_order(root.right)

# Driver program to test the above functions
# Let us create the following BST
#       50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80

r = Node(50)
insert(r, 30)
insert(r, 20)
insert(r, 40)
insert(r, 70)
insert(r, 60)
insert(r, 80)

print('-----------Traversal-----------')
in_order(r)

print('')
print('-------------search 2--------------')
print(search(r, 2))

print('-------------search 70--------------')
print(search(r, 70))
