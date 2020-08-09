"""
Binary Search Tree is a node-based binary tree data structure which has the following properties:
    1. The left subtree of a node contains only nodes with keys lesser than the node’s key.
    2. The right subtree of a node contains only nodes with keys greater than the node’s key.
    3. The left and right subtree each must also be a binary search tree. There must be no duplicate nodes.

                                           8
                                        /     \
                                     3          10
                                   /   \           \
                                 1       6          14
                                       /   \       /
                                     4      7    13

The above properties of Binary Search Tree provide an ordering among keys so that the operations like search,
minimum and maximum can be done fast. If there is no ordering, then we may have to compare every key to search
a given key.

Binary Search Tree works like a sorted array.
"""