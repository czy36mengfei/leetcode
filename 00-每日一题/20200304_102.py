 # 二叉树的层次遍历
# 使用队列
from leetcode.tree_node import TreeNode, get_binary_tree


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            cur = []
            length = len(queue)
            # 遍历层
            for i in range(length):
                node = queue.pop(0)
                cur.append(node.val)
                left = node.left
                right = node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            res.append(cur)
        return res


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        node_list = [int(n) if n != 'null' else None for n in nums_str]
        root = get_binary_tree(node_list)
        res = obj.levelOrder(root)
        print(res)



