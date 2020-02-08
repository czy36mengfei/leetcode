class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length=len(nums)
        if length <= 1:
            return True

        max_arrive = 0
        for i in range(length):
            if i > max_arrive:
                return False
            else:
                max_arrive = max(max_arrive, i+nums[i])
        return True
