from leetcode.tree_node import TreeNode, get_binary_tree

class Solution:
    def preorder(self, node, val):
        # 终止条件
        if node is None:
            return False

        if node.val == val:
            return True

        if self.preorder(node.left, val) or self.preorder(node.right, val):
            return True
        return False
