# 路径总和
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        self._dfs(root, [], sum, res)
        return res


    def _dfs(self, node, path, last, res):
        if node.left is None and node.right is None:
            if last == node.val:
                path.append(node.val)
                res.append(path[:])
                path.pop()
            return
        path.append(node.val)
        if node.left:
            self._dfs(node.left, path, last-node.val, res)
        if node.right:
            self._dfs(node.right, path, last-node.val, res)
        path.pop()  # 该节点遍历后退出

