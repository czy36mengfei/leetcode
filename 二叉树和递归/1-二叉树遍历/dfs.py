# 求二叉树深度，dfs
from leetcode.tree_node import TreeNode, get_binary_tree, print_binary_tree

class Solution(object):
    def __init__(self):
        self.depth = 0

    def _dfs(self, root, depth):
        # 无节点
        if root is None:
            return

        # 有节点，标记该节点深度
        depth += 1
        # 该节点为叶子节点
        if root.left is None and root.right is None:
            # 更新最大深度
            self.depth = max(depth, self.depth)
            return
        if root.left:
            self._dfs(root.left, depth)
        if root.right:
            self._dfs(root.right, depth)

    def _maxDepth2(self, root):
        # DFS
        if root is None:
            return 0
        self._dfs(root, 0)
        return self.depth

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nodes = [int(n) if n != 'null' else None for n in nums_str]
        root = get_binary_tree(nodes)
        res = obj._maxDepth2(root)
        print(res)