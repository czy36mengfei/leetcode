from leetcode.tree_node import TreeNode, get_binary_tree, print_binary_tree

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self._isBalanced(root) != -1
    def _isBalanced(self, node):
        # 后序遍历
        if node is None:
            return 0
        left = self._isBalanced(node.left)
        right = self._isBalanced(node.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        return max(left, right) +1


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nodes = [int(n) if n != 'null' else None for n in nums_str]
        root = get_binary_tree(nodes)
        res = obj.isBalanced(root)
        print(res)
