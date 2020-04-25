# 二叉树的锯齿形层次遍历
from leetcode.tree_node import TreeNode, get_binary_tree
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return []

        queue = [root]
        left_direction = False
        while(queue):
            length = len(queue)
            cur = []
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if left_direction:
                    cur.insert(0, node.val)
                else:
                    cur.append(node.val)
            res.append(cur)
            left_direction = not left_direction
        return res

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        node_list = [int(n) if n != 'null' else None for n in nums_str]
        root = get_binary_tree(node_list)
        res = obj.zigzagLevelOrder(root)
        print(res)






