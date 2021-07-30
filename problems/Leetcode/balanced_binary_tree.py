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


class Solution:
    """
    1: Are my left and right child balanced,
    2: what's my height
    """

    def isBalanced(self, root: TreeNode) -> bool:
        # base case
        if root == None:
            return {"height": -1, "balanced": True}
        difference = abs(self.isBalanced(root.left)[
                         "height"]-self.isBalanced(root.right)["height"])
        if difference <= 1:
            return {"height": 45, "balanced": True}


soli = Solution()
soli.isBalanced(rooti)
