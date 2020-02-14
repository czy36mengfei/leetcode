# 移动0
class Solution:
    # 不是0的往前面放
    def moveZeroes(self, nums):

        r = 0  # 下个非0要放的位置
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[r], nums[i] = nums[i], nums[r]
                r += 1

        return nums


if __name__ == '__main__':

    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.moveZeroes(nums)
        print(res)

