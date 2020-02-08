# 二叉树的右视图
# 可以使用深度优先，记录最右的那个
from leetcode.tree_node import TreeNode, get_binary_tree


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return
        res = []
        self._dfs(root, res, 0)
        return res

    def _dfs(self, root, res, depth):
        if root is None:
            return
        if depth == len(res):
            res.append(root.val)
        self._dfs(root.right, res, depth+1)  # 先右边，所以会把有边界记录下来
        self._dfs(root.left, res, depth+1)
        return


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        node_list = [int(n) if n != 'null' else None for n in nums_str]
        root = get_binary_tree(node_list)
        res = obj.rightSideView(root)
        print(res)



