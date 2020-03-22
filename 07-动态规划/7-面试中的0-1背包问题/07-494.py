# P-Q = S
# P+Q = sum(nums)
# 2P = S + sum(nums)


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        sum_nums = sum(nums)
        target = sum(nums) + S
        if target % 2 == 1:
            return 0
        else:
            target = target // 2
        if sum_nums < target:
            return 0

        dp = [0 for _ in range(target+1)]
        dp[0] = 1  # 剩余的全部是也是一种， 用于填满背包
        # 里面可能存在0
        for c in range(target+1):
            if nums[0] == c:
                dp[c] += 1

        for i in range(1, length):
            for c in range(target, -1, -1):  # 里面可能存在0
                # 可以选该物品
                if nums[i] <= c:
                    dp[c] = dp[c] + dp[c-nums[i]]
        return dp[-1]

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        S = int(input().strip())
        res = obj.findTargetSumWays(nums, S)
        print(res)