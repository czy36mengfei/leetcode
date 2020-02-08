from leetcode.tree_node import TreeNode


def build_a_BST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    length = len(nums)
    if length == 0:
        return None
    return r_build(nums, 0, length-1)


def r_build(nums, left, right):
    # 递归停止条件
    if left > right:
        return None
    if left == right:
        return TreeNode(nums[left])

    # 二分搜索
    mid = (left+right) // 2
    root = TreeNode(nums[mid])
    root.left = r_build(nums, left, mid-1)
    root.right = r_build(nums, mid+1, right)
    return root