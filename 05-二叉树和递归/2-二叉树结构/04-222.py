from leetcode.tree_node import TreeNode, get_binary_tree, print_binary_tree

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_depth = self._depth(root, is_left=True)
        right_depth = self._depth(root, is_left=False)
        if left_depth == right_depth:
            # left_depth ** 2 -1
            return (1 << left_depth) - 1
        return self.countNodes(root.left) + self.countNodes(root.right)+1


    def _depth(self, root, is_left):
        # 看最左侧或最右侧来看深度
        depth = 0
        node = root
        while node:
            if is_left:
                node = node.left
                depth += 1
            else:
                node = node.right
                depth += 1
        return depth


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nodes = [int(n) if n != 'null' else None for n in nums_str]
        root = get_binary_tree(nodes)
        res = obj.countNodes(root)
        print(res)