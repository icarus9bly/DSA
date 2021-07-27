# Resources:
- https://sapient.udemy.com/course/python-for-data-structures-algorithms-and-interviews/
- https://github.com/ombharatiya/FAANG-Coding-Interview-Questions
- https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/tree/master/
- https://www.youtube.com/watch?v=BHB0B1jFKQc | Binary Tree

# Recursion:
- import functools; functools.lru_cache() # For Memoization/caching
- recursion makes use of call stack.
- Call stack remembers all the variables in a function call and when recusrion hits the base case all variables are poped off frame by frame doing some operation.
# Tree:
- Types:
  - Full: If the tree has either two child nodes or none.
  - Complete: If we fill the binary tree from top to bottom and left to right. E.g. Binary Heap
  - Perfect: If our tree is both Full and complete, it's Perfect BT.
- [root,left,right] e.g. [3,[],[]]
- Insert left child:
  - [3,[4,[],[]],[]] # If left child is empty
  - [3,[4,[3,[],[]],[]],[]] # If left child is not empty the OG branch goes down to be the left child of newly inserted branch.

# Tree Traversels:
- left and right will always be the same just visiting root changes with prefix for e.g. pre: n|r, In: |nr, Post: |rn (|-> left subtree, n-> node, r-> right subtree)
- Pre-order: Visit the root node first, then the left child, then the right child
- In-order: Visit the left child first, then the root, then the right child
- Post-order: Visit the left child first, then the right child, then the root node.

# Binary Heap:
- If we want the **"largest"** item we want **"min-heap"** and if **"smallest"** item we want **"max-heap"**
