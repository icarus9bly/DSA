# Python program to introduce Binary Tree

# A class that represents an individual node in a
# Binary Tree
class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# create root
root = Tree(1)
''' following is the tree after above statement
		1
	/ \
	None None'''

root.left = Tree(2)
root.right = Tree(3)

''' 2 and 3 become left and right children of 1
		1
		/ \
		2	 3
	/ \ / \
None None None None'''


root.left.left = Tree(4)
'''4 becomes left child of 2
		1
	   / \
	  /   \
	 2	   3
    / \    /\
   /   \  /  \
  4 None None None
 / \
None None'''

# rootNonOOP = [1, [2, [4, None, None], None], [3, None, None]]

print(root.val)


# iteratively
def inorder_traversal(root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right


print(inorder_traversal(root))
