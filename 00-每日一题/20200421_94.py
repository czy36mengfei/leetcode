# 二叉树的后序遍历
# 使用系统栈
from leetcode.tree_node import TreeNode, get_binary_tree


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        # 1需要访问孩子
        # 0访问自己
        stack = [(1, root)]
        res = []
        while stack:
            state, node = stack.pop()
            if state == 1:
                if node.right:
                    stack.append((1, node.right))
                # 中序， 访问完左子树后访问根
                stack.append((0, node))  # 访问完左子树后访问
                if node.left:
                    stack.append((1, node.left))
            else:
                res.append(node.val)
        return res



if __name__ == '__main__':
    obj = Solution()
    while True:
        node_list_str = input().strip().split()
        node_list = [int(v) if v != 'null' else None for v in node_list_str]
        root = get_binary_tree(node_list)
        res = obj.inorderTraversal(root)
        print(res)



