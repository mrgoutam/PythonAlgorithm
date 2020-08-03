"""
Given a binary tree and a key, insert the key into the binary tree at first position available in Level Order.

                  10                                          10
                /    \          After inserting            /      \
             11       9         -------------->          11        9
             /       /  \                              /    \     /   \
            7       15   8                           7       12  15    8

"""

class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


# in-order traversal of binary tree
def in_order(temp):
    if temp is None:
        return
    in_order(temp.left)
    print(temp.key, end=" ")
    in_order(temp.right)

def insert(temp, key):
    q = [temp]

    # doing level order traversal until we find an empty place
    while len(q):
        temp = q[0]
        q.pop(0)
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

if __name__=='__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print('Before insertion: ', end=' ')
    in_order(root)

    key = 12
    insert(root, key)

    print()
    print('After insertion: ', end=' ')
    in_order(root)

