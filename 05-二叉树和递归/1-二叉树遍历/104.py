# 求二叉树深度，类似后序遍历
from leetcode.tree_node import TreeNode, get_binary_tree, print_binary_tree

class Solution(object):
    def __init__(self):
        self.depth = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        return max(l_depth, r_depth) + 1

    def _maxDepth(self, root):
        # BFS
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            size = len(queue)  # BFS的关键就是记录每一层的数量
            depth += 1
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

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