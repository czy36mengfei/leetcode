# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        res = max(self.r_rob(root))
        return res
    def r_rob(self, root):

        if root is None:
            return [0, 0]

        left = self.r_rob(root.left)
        right = self.r_rob(root.right)
        # res1不包含根节点， res2包含根节点
        res1 = max(left) + max(right)  # 不包含根节点，孩子的情况取什么都可以
        res2 = left[0] + right[0] + root.val #  包含根节点，孩子不能有根节点
        return [res1, res2]

    def __rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)
        return max(res, self.rob(root.left) + self.rob(root.right))