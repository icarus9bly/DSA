# https://leetcode.com/problems/map-sum-pairs/

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        root = self.root
        for w in key:
            if w not in root:
                root[w] = {}
            root = root[w]
        root["-"] = val

    def get_siblings(self, prefix):
        root = self.root
        for w in prefix:
            if w not in root:
                return None
            root = root[w]
        return root

    def get_sum(self, root):
        cost = 0
        for w in root:
            if w == "-":
                cost += root[w]
                continue
            cost += self.get_sum(root[w])
        return cost

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        root = self.get_siblings(prefix)
        if root:
            return self.get_sum(root)
        return 0
