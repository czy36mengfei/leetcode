class MapSum(object):
    class Node:
        def __init__(self):
            self.val = 0
            self.dict = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = MapSum.Node()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        node = self.root
        for c in key:
            if c not in node.dict:
                node.dict[c] = MapSum.Node()

            node = node.dict[c]
        node.val = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for c in prefix:
            if c not in node.dict:
                return 0
            else:
                node = node.dict[c]
        res = self.get_sum(node)
        return res

    def get_sum(self, node):
        res = 0
        res += node.val
        for next in node.dict:
            res += self.get_sum(node.dict[next])
        return res
