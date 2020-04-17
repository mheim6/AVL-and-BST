Monica Heim
Wednesday, March 20, 2019
Data Structures and Algorithms

README

							
__________________________________________________________________________________________________

Binary search trees
keeps their keys in sorted order so that lookup and other operations can use the principle of binary search: when looking for a key in a tree (or a place to insert a new key), they traverse the tree from root to leaf, making comparisons to keys stored in the nodes of the tree and deciding, on the basis of the comparison, to continue searching in the left or right subtrees. On average, this means that each comparison allows the operations to skip about half of the tree, so that each lookup, insertion or deletion takes time proportional to the logarithm of the number of items stored in the tree. This is much better than the linear time required to find items by key in an (unsorted) array, but slower than the corresponding operations on hash tables.

AVL tree
was named after Adelson-Velsky and Landis. This tree is a self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases, where n is the number of nodes in the tree prior to the operation. Insertions and deletions may require the tree to be rebalanced by one or more tree rotations. 

Balancing Operations used in AVL:
If tree is out of balance meaning that it's left and right subtrees height differ by more than abs(1) then we need to rebalance it.
Balancing is done by single left or right rotations or with double left or right rotations of the tree. The tree can be rotate left or right.
With left rotation, right subtree root replaces current root. With right rotation, left subtree replaces current root. Leaves can be deleted immediately. If tree only has left or right subtree, it's replaced with one of them. In the worst case scenario the tree has both left and right subtrees. If this happened the program will need to find a logical successor or predecessor. Successor is its smallest node in its right subtree. Predecessor is it's largest node in left subtree.



Data Points:
hw4-sample1.txt---
THIS IS BST
Height of BST tree is :  5
Total Duplicates:  0
Total Inserted:  10
THIS IS AVL
Height of AVL tree is:  5
Total Duplicates:  0
Total Inserted:  10

hw4-sample2.txt---
THIS IS BST
Height of BST tree is :  12
Total Duplicates:  1
Total Inserted:  49
THIS IS AVL
Height of AVL tree is:  7
Total Duplicates:  1
Total Inserted:  49

hw4-sample3.txt---
THIS IS BST
Height of BST tree is :  18
Total Duplicates:  5
Total Inserted:  145
THIS IS AVL
Height of AVL tree is:  9
Total Duplicates:  5
Total Inserted:  145

hw4-sample4.txt---
THIS IS BST
Height of BST tree is :  22
Total Duplicates:  62
Total Inserted:  938
THIS IS AVL
Height of AVL tree is:  12
Total Duplicates:  62
Total Inserted:  938

hw4-sample5.txt---
THIS IS BST
Height of BST tree is :  32
Total Duplicates:  657
Total Inserted:  4343
THIS IS AVL
Height of AVL tree is:  15
Total Duplicates:  657
Total Inserted:  4343

hw4-sample5.txt deleteme.txt---
THIS IS BST
Height of BST tree is :  32
Total Duplicates:  657
Total Inserted:  4343
THIS IS AVL
Height of AVL tree is:  15
Total Duplicates:  657
Total Inserted:  4343
Deletes:  100







