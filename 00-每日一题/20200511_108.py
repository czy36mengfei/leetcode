from leetcode.tree_node import TreeNode
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return None
        return self._help(nums, 0, length-1)

    def _help(self, nums, left, right):
        # 递归停止条件
        if left > right:
            return None
        if left == right:
            return TreeNode(nums[left])

        # 二分搜索
        mid = (left+right) // 2
        root = TreeNode(nums[mid])
        root.left = self._help(nums, left, mid-1)
        root.right = self._help(nums, mid+1, right)

        return root