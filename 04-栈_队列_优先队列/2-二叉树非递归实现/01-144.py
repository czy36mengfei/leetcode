# 掌握前序遍历，使用栈的写法

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 教前序遍历非递归写法

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        stack = [root]

        while stack:
            node = stack.pop()  # 先遍历父节点
            if node.right:
                stack.append(node.right)
            if node.left:  # 后压左，先遍历左树
                stack.append(node.left)
            res.append(node.val)
        return res

