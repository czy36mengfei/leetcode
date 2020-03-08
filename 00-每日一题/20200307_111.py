# 求二叉树最小深度
from leetcode.tree_node import TreeNode, get_binary_tree, print_binary_tree
import sys
class Solution(object):
    def __init__(self):
        self.depth = sys.maxsize
    # 类似后序遍历
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # 深度是由叶子节点觉得的， 叶子节点没左也没右孩子。
        # 已知没左就看其右，已知没右，就看其左
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # BFS
    def _minDepth(self, root):
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    # DFS, 类似前序遍历
    def _dfs(self, root, depth):
        if root is None:
            return
        depth += 1
        if root.left is None and root.right is None:
            self.depth = min(depth, self.depth)
        if root.left:
            self._dfs(root.left, depth)
        if root.right:
            self._dfs(root.right, depth)

    def _minDepth2(self, root):
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
        res = obj._minDepth2(root)
        print(res)