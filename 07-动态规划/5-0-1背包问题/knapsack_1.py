class Solution:
    def knapsack01(self, weights, values, capacity):
        length = len(weights)
        if length == 0:
            return 0
        dp = [[0 for _ in range(capacity+1)] for _ in range(length)]

        # 第一行直接赋值
        for c in range(1, capacity+1):
            if weights[0] <= c:
                dp[0][c] = values[0]
            else:
                dp[0][c] = 0

        for i in range(1, length):
            for c in range(1, capacity+1):
                # 可以放入当前物品
                if weights[i] <= c:
                    # 除了该物品的容积用前一行的
                    dp[i][c] = values[i] + dp[i-1][c-weights[i]]
                else:
                    # 不放物品就直接copy上一行
                    dp[i][c] = dp[i-1][c]
        return dp[-1][-1]
    # 压缩成一行
    def _knapsack01(self, weights, values, capacity):
        length = len(weights)
        if length == 0:
            return 0
        dp = [0 for _ in range(capacity+1)]
        for c in range(1, capacity+1):
            if weights[0] <= c:
                dp[c] = values[0]

        for i in range(1, length):
            # 逆着来，这样同一行被修改后，后面不会再动
            # 每一次只会参考前面的
            for c in range(capacity, 0, -1):
                dp[c] = max(dp[c], values[i] + dp[c-weights[i]])  # c位置和c-weights位置都是前一行
        return dp[-1]



if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        nums2_str = input().strip().split()
        nums2 = list(map(int, nums2_str))
        c = int(input().strip())
        res = obj._knapsack01(nums, nums2, c)
        print(res)

