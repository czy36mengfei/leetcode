# 状态转移方程
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length <= 3:
            return max(nums)

        res1 = self.single_rob(nums[:-1])
        res2 = self.single_rob(nums[1:])
        res = max(res1, res2)
        return res

    def single_rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length <= 2:
            return max(nums)

        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            # 分为当前的偷和不偷
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[length - 1]


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.rob(nums)
        print(res)
