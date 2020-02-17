class Solution(object):
    def removeDuplicates(self, nums):
        length = len(nums)

        if length < 2:
            return length

        j = 1

        for i in range(2, length):
            if nums[i] != nums[j-1]:
                j = j+1
                nums[j] = nums[i]

        return j + 1
