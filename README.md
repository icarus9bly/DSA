# Resources:

- [DSA Course python udemy](https://sapient.udemy.com/course/python-for-data-structures-algorithms-and-interviews/)
- [FAANG-Coding-Questions](https://github.com/ombharatiya/FAANG-Coding-Interview-Questions)
- https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/tree/master/
- [Binary Tree](https://www.youtube.com/watch?v=BHB0B1jFKQc)
- [Big-O Cheatsheet](https://www.bigocheatsheet.com/)

# Abstract data types:

- Data types we define with a set of roles to model our data like stacks and queues.
- **Stack** have rules push and pop
- **Queue** have rules enqueue and dequeue.
- **Priority queue** have rules insert_with_priority, pull_highest_priority_item.

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
- Array representation of Binary Tree:
  - In this array arr = [3,9,20,null,null,15,7], 3 is the root node, 9 and 20 are left and right, null,null,15,7 are filled left to right below 9 and 20.
  - Formula:
    - Where n is the current index starting from 0.
    - These only holds for complete binary tree.
    -  To find out parent of current node: (n-1)/2 
    -  To find out children:
      -   left child: (2*n)+1
      -   right child: (2*n)+2

# Tree Traversels:

- left and right will always be the same just visiting root changes with prefix for e.g. pre: n|r, In: |nr, Post: |rn (|-> left subtree, n-> node, r-> right subtree)
- Pre-order: Visit the root node first, then the left child, then the right child
- In-order: Visit the left child first, then the root, then the right child
- Post-order: Visit the left child first, then the right child, then the root node.

# Binary Heap:
- Steps to follow:
  1. Insert in heap (Top to bottom left to right)
  2. Restore the heap by comparing inserted item with parent node and sorting.
  3. Remove/peeking a item:
  - Replace the root parent with last child.
  - Replace the new parent with child nodes by comparing it with child nodes.
- Constant time **0(1)** for peeking, for inserting and removing and item **0(logn)**
- **Pro-tip:** If we want the **"largest"** kth item we want **"min-heap"** and if **"smallest"** item we want **"max-heap"**

# Sort:
- **Quick Sort:**
  - Two subroutines are:
    - Split
    - Partioning to choose a pivot (Pivot is the item we want to find the position of.)
  - Select Left(arr[0]) and Right(arr[-1])
  - Randomaly select pivot
