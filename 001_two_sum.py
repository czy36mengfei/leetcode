
"""
    ====== 001 two sum ======
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.


    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        pre_nums = {}
        for i, num in enumerate(nums):
            if target-num in pre_nums:
                return [pre_nums[target-num], i]
            pre_nums[num] = i
        return []

if __name__ == '__main__':
    obj = Solution()
    nums_str = input().strip()
    nums = list(map(int, nums_str.split()))
    target = int(input().strip())
    res = obj.two_sum(nums, target)
    print(res)






