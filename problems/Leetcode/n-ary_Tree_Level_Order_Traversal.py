# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            temp = []
            next_queue = []
            for node in queue:
                temp.append(node.val)
                for child in node.children:
                    next_queue.append(child)
            queue = next_queue
            res.append(temp)
        return res
