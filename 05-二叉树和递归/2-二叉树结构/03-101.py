# 对称二叉树
"""
    1
   / \
  2   2
 / \ / \
3  4 4  3
"""
class Solution(object):

    def _isSymmetric(self, left, right):
        # left, right为实际中要对称的点
        if left is None and right is None:
            return True
        if left is None or right is None or right.val != left.val:
            return False
        return self._isSymmetric(left.right, right.left) and self._isSymmetric(left.left, right.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self._isSymmetric(root.left, root.right)



