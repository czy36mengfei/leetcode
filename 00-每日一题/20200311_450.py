class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        # key在子树中
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            # key匹配当前节点
            # 左子树为空
            if root.left is None:
                return root.right
            # 右子树为空
            if root.right is None:
                return root.left

            # 以后继替换（右子树最左点）
            successor = self.get_successor(root.right)

            successor.right = self.del_successor(root.right)
            successor.left = root.left
            return successor

    def get_successor(self, root):
        while root.left:
            root = root.left
        return root  # 没有左也子的那一个为最左端


    def del_successor(self, root):

        if root.left is None:
            return root.right  # 把右树放过去
        root.left = self.del_successor(root.left)
        return root







