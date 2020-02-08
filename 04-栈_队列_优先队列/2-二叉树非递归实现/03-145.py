# 二叉树的后续遍历
# 使用系统栈
from leetcode.tree_node import TreeNode, get_binary_tree
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return None
        # 1表示还没有弹出孩子，0表示已经弹出孩子，可以访问
        stack = [(1, root)]
        res = []
        while stack:
            state, node = stack.pop()
            if state == 1:
                stack.append((0, node))  # 访问完右子树后访问父节点
                if node.right:
                    stack.append((1, node.right))
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
        res = obj.postorderTraversal(root)
        print(res)



