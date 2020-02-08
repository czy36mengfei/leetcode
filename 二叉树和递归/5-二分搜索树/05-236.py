class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root  # 没有

        if root == p or root == q:
            # 返回匹配的点， 如果一个点在另一个点的子树种，只返回前一个点
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            # 左右都有当前点就是
            return root
        elif left:
            # 只有左边有
            return left
        elif right:
            return right
        else:
            return None

