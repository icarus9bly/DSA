# https://leetcode.com/problems/balanced-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = [3, 9, 20, None, None, 15, 7]

rooti = TreeNode(3)
rooti.left = TreeNode(9)
rooti.right = TreeNode(20)
rooti.right.left = TreeNode(15)
rooti.right.right = TreeNode(7)
# rooti.right.right.right = TreeNode(7)


class Solution:
    """
    1: Are my left and right child balanced,
    2: what's my height
    """

    def isBalanced(self, root):

        def check(root):
            # base case
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


soli = Solution()
print(soli.isBalanced(rooti))
