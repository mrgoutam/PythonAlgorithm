"""
#### NEED TO UNDERSTAND PROPERLY- Goutam D
three possibilities arise.
1. Node to be deleted is leaf: Simply remove from the tree.

              50                             50
           /     \         delete(20)      /   \
          30      70       --------->    30     70
         /  \    /  \                     \    /  \
       20   40  60   80                   40  60   80

2. Node to be deleted has only one child: Copy the child to the
node and delete the child

              50                            50
           /     \         delete(30)      /   \
          30      70       --------->    40     70
            \    /  \                          /  \
            40  60   80                       60   80

3. Node to be deleted has two children: Find inorder successor of the node.
Copy contents of the inorder successor to the node and delete the inorder
successor. Note that inorder predecessor can also be used.

              50                             60
           /     \         delete(50)      /   \
          40      70       --------->    40    70
                 /  \                            \
                60   80                          80

"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def in_order(root_):
    if root_:
        in_order(root_.left)
        print(root_.data, end=' ')
        in_order(root_.right)

def insert(root_, key):
    mNode = Node(key)
    if root_ is None:
        root_ = mNode
    else:
        if root_.data < mNode.data:
            if root_.right is None:
                root_.right = mNode
            else:
                insert(root_.right, key)
        else:
            if root_.left is None:
                root_.left = mNode
            else:
                insert(root_.left, key)
    return root_

# Given a non-empty binary search tree, return the node
# with minimum key value found in that tree.
def minValueNode(root_):
    current = root_
    # loop down to find the left most leaf
    while current.left is not None:
        current = current.left
    return current

def delete(root_, key):

    if root_ is None:
        return root_

    # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if key<root_.data:
        root_.left = delete(root_.left, key)

    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif key>root_.data:
        root_.right = delete(root_.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        # Node with only one child or no child
        if root_.left is None:
            temp = root_.right
            root_ = None
            return temp
        elif root_.right is None:
            temp = root_.left
            root_ = None
            return temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root_.right)

        # Copy the inorder successor's content to this node
        root_.key = temp.key

        # Delete the inorder successor
        root_.right = deleteNode(root_.right, temp.key)

    return root# Driver program to test above functions
""" Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print ("Inorder traversal of the given tree")
in_order(root)

print ("\nDelete 20")
root = delete(root, 20)
print ("Inorder traversal of the modified tree")
in_order(root)

print ("\nDelete 30")
root = delete(root, 30)
print ("Inorder traversal of the modified tree")
in_order(root)

print ("\nDelete 50")
root = delete(root, 50)
print ("Inorder traversal of the modified tree")
in_order(root)