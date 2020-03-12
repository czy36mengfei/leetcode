# 验证二叉搜索树

# 使用中序遍历
import sys
class Solution(object):
    pre_val = -sys.maxsize
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self._isValidBST(root)

    def _isValidBST(self, root):
        if root.left:
            # 左侧为二叉搜索树
            left = self._isValidBST(root.left)
            if left is False:
                return False

        # 每个节点小于他前一个节点  -- 中序遍历
        if self.pre_val >= root.val:
            return False
        self.pre_val = root.val
        if root.right:
            # 右侧为二叉搜索树
            right = self._isValidBST(root.right)
            if right is False:
                return False
        return True


