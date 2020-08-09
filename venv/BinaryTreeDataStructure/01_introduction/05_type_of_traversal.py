"""
Unlike linear data structures(Array, LinkedList, Queue, Stacks etc) which have only one logical way to traverse then,
trees can be traversed in different ways.

                       1
                    /    \
                  2       3
                /   \
              4      5
Depth First Traversals:
 1. In-Order(Left, Root, Right) : 4 2 5 1 3
 2. Pre-Order(Root, Left, Right) : 1 2 4 5 3
 3. Post-Order(Left, Right, Root) : 4 5 2 3 1
"""