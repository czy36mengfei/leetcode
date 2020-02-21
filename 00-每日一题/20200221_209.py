# 滑动窗口
class Solution:
    def minSubArrayLen(self, s, nums):

        length = len(nums)
        if length == 0:
            return 0

        res = length + 1
        sum = 0
        l = 0
        for r in range(length):
            sum += nums[r]
            while sum >= s:
                res = min(res, r-l+1)
                sum -= nums[l]
                l += 1
        if res == length + 1:
            return 0
        return res


if __name__ == '__main__':

    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        s = int(input().strip())
        res = obj.minSubArrayLen(s, nums)
        print(res)
