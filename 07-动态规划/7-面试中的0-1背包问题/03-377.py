class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        dp = [0 for _ in range(target+1)]

        dp[0] = 1
        for i in range(1, target+1):

            for j in range(length):
                if nums[j] <= i:
                    dp[i] += dp[i-nums[j]]

        return dp[-1]

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        target = int(input().strip())
        res = obj.combinationSum4(nums, target)
        print(res)
