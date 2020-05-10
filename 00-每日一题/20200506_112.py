# 路径之和

from leetcode.tree_node import TreeNode

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        left = self.hasPathSum(root.left, sum-root.val)
        right = self.hasPathSum(root.right, sum-root.val)

        return left or right

