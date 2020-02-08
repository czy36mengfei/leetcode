from leetcode.tree_node import TreeNode, get_binary_tree

class Solution:
    def preorder(self, node):
        # 终止条件
        if node is None:
            return
        print(node.val)
        # 递归
        self.preorder(node.left)
        self.preorder(node.right)
