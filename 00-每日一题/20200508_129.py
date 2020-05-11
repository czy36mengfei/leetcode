# 求根到叶子节点数字之和

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = []
        self._dfs(root, 0, res)
        return sum(res)

    def _dfs(self, root, pre_v, res):

        if root.left is None and root.right is None:
            # 直接把前面的结果乘以10
            res.append(pre_v*10+root.val)
        if root.left:
            self._dfs(root.left, pre_v*10+root.val, res)
        if root.right:
            self._dfs(root.right, pre_v*10+root.val, res)