# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root2 = Tree(5)
root2.right = Tree(3)

root1 = Tree(1)
root1.right = Tree(3)


class Solution:
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q


comp = Solution()
print(comp.isSameTree(root1, root2))
