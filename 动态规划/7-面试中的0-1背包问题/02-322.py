import sys


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        length = len(coins)
        if length == 0:
            return -1

        dp = [0 for _ in range(amount+1)]
        for i in range(1, amount+1):
            min_val = sys.maxsize
            for j in range(len(coins)):
                if coins[j] <= i and dp[i-coins[j]] != -1:  # 放入这个后，其他的可填满
                    min_val = min(min_val, 1+dp[i-coins[j]])
            if min_val == sys.maxsize:
                dp[i] = -1
            else:
                dp[i] = min_val
        return dp[-1]


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        amount = int(input().strip())
        res = obj.coinChange(nums, amount)
        print(res)