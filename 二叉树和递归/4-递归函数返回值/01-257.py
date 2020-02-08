# 二叉树的所有路径
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root is None:
            return res
        self._dfs(root, '', res)
        return res


    def _dfs(self, root, pre, res):

        # 终结条件-叶子节点
        if root.left is None and root.right is None:
            res.append(pre+str(root.val))

        if root.left:
            self._dfs(root.left, pre+str(root.val)+'->', res)

        if root.right:
            self._dfs(root.right, pre+str(root.val)+'->', res )
