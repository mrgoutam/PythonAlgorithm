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

def insert(temp, key_val):
    q = [temp]

    # doing level order traversal until we find an empty place
    while len(q):
        temp = q[0]
        q.pop(0) # removing 0th element
        if temp.left is None:
            temp.left = Node(key_val)
            break
        else:
            q.append(temp.left)

        if temp.right is None:
            temp.right = Node(key_val)
            break
        else:
            q.append(temp.right)

"""
Step by step description:
1. q = [temp] 
    creating a queue with root Node(10). Length of queue is 1.
2. while len(q):
    true because length of the queue is not 0 and it is 1. Now we are inside while.
Iteration 1:
    1. temp = q[0]
        here temp is equal to Node(10).
    2. q.pop(0)
        removing 0th element. Now q is empty.
    3. if temp.left is None:
        the condition is false as Node(10) has left node Node(11). So, inside else part 'q.append(temp.left)'
        will execute. Now q has one node that is Node(11)
    4. if temp.right is None:
        the condition is false as Node(10) has right node Node(9). So, inside else part 'q.append(temp.right)'
        will execute. Now q has two nodes that are Node(11) and Node(9).
    end of Iteration 1.
Iteration 2:
    now q = [Node[11], Node[9]].
    1. temp = q[0]
        here temp is equal to Node(11).
    2. q.pop(0)
        removing 0th element. Now q = [Node[9]].
    3. if temp.left is None:
        the condition is false as Node(11) has left node Node(7). So, inside else part 'q.append(temp.left)'
        will execute. Now q = [Node[9], Node[7]]
    4. if temp.right is None:
        the condition is true as Node(11) has no node at right. the node Node(12) will be added at right. Break
        statement will break the loop.
    end of Iteration 2.
"""

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

