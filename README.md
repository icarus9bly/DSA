# Resources:
- https://sapient.udemy.com/course/python-for-data-structures-algorithms-and-interviews/
- https://github.com/ombharatiya/FAANG-Coding-Interview-Questions
- https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/tree/master/
- https://www.youtube.com/watch?v=BHB0B1jFKQc | Binary Tree

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
- Pre-order: Visit the root node first, then the left child, then the right child
- In-order: Visit the left child first, then the root, then the right child
- Post-order: Visit the left child first, then the right child, then the root node.
