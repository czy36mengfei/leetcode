# 求二叉树深度，bfs
from leetcode.tree_node import TreeNode, get_binary_tree, print_binary_tree

class Solution(object):
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


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nodes = [int(n) if n != 'null' else None for n in nums_str]
        root = get_binary_tree(nodes)
        res = obj._maxDepth(root)
        print(res)