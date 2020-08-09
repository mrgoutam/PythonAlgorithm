"""
The following are the common types of binary tree.

Full Binary Tree:
  A Binary tree is full binary tree if every node has 0 or 2 children. We can also say a full binary
tree is a binary tree in which all nodes except leaf nodes have two children.

                           18
                       /       \
                     15         30
                    /  \        /  \
                  40    50    100   40

                         18
                       /    \
                     15     20
                    /  \
                  40    50
                /   \
               30   50

                           18
                        /     \
                      40       30
                               /  \
                             100   40

In a Full Binary Tree, number of leaf nodes is the number of internal nodes plus 1.
               L = i + 1
               where L = Number of Leaf Nodes
                     i = Number of Internal Nodes

Complete Binary Tree:
  A Binary Tree is a complete Binary Tree if all the levels are completely filled except the
last level and the last level has all the keys as left as possible.

                           18
                       /       \
                     15         30
                    /  \        /  \
                  40    50    100   40


                           18
                       /       \
                     15         30
                    /  \        /  \
                  40    50    100   40
                 /  \   /
                8   7  9

Perfect Binary Tree:
  A Binary Tree is a Perfect Binary Tree in which all the internal nodes have two children and
all the leaf nodes are at the same level.

                           18
                       /       \
                     15         30
                    /  \        /  \
                  40    50    100   40


                           18
                       /       \
                     15         30

A Perfect Binary Tree of height h ( where height is the number of nodes on the path from the root to leaf) has
2^h-1 nodes.

Balances Binary Tree:
  A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes.
Example: AVL tree, Red-Black tree

Degenerate(or pathological) tree:
  A tree where every internal node has one child. Such trees are performance-wise same as liked list.

                    10
                  /
                20
                 \
                 30
                  \
                  40
"""