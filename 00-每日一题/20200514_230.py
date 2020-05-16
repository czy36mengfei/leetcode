# 二叉搜索树第k小元素
import sys
class Solution(object):
    num = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.num = 0
        return self._help(root, k)

    def _help(self, root, k):
        if root is None:
            return sys.maxsize
        left = self._help(root.left, k)
        if left != sys.maxsize:
            return left
        self.num += 1
        if self.num == k:
            return root.val
        right =self._help(root.right, k)
        if right != sys.maxsize:
            return right
        return sys.maxsize

    # 使用系统栈的方法
    def _kthSmallest(self, root, k):
        stack = [(1, root)]
        while stack:
            command, node = stack.pop()
            if command == 0:  # 访问command为0的节点
                k -= 1
                if k ==0:
                    return node.val
            else: # 访问command为1的节点
                # 因为是栈，所以先放right
                if node.right:
                    stack.append((1, node.right))
                stack.append((0, node))

                if node.left:
                    stack.append((1, node.left))


