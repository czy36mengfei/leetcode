class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)

        sum_num = sum(nums)
        if sum_num % 2 == 1:
            return False
        half = sum_num // 2
        dp = [[False for _ in range(half+1)] for _ in range(length)]

        # 第一行
        for c in range(half+1):
            if c == nums[0]:
                dp[0][c] = True

        # 下面各行
        for i in range(1, length):
            for c in range(half+1):
                if nums[i] <= c:
                    # dp[i-1][c] 不放当前的
                    # dp[i-1][c-nums[i]] 放当前的
                    # 两个只要一个可以就行
                    dp[i][c] = dp[i-1][c] or dp[i-1][c-nums[i]]
                else:
                    dp[i][c] = dp[i - 1][c]  # 有的可以不用
        return dp[-1][-1]

    def _canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)

        sum_num = sum(nums)
        if sum_num % 2 == 1:
            return False
        half = sum_num // 2
        dp = [False for _ in range(half+1)]

        # 第一行
        for c in range(half+1):
            if c == nums[0]:
                dp[c] = True

        # 下面各行
        for i in range(1, length):
            for c in range(half, 0, -1):
                if nums[i] <= c:
                    # dp[i-1][c] 不放当前的
                    # dp[i-1][c-nums[i]] 放当前的
                    # 两个只要一个可以就行
                    dp[c] = dp[c] or dp[c-nums[i]]

        return dp[-1]

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj._canPartition(nums)
        print(res)