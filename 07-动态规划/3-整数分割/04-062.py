class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self._combination(m+n-2, m-1)

    def _factorial(self, x):
        # 阶乘
        res = 1
        for i in range(2,x+1):
            res *= i
        return res

    def _combination(self, a, b):
        # a个数选择b个
        return self._factorial(a) // (self._factorial(b) * self._factorial(a-b))

    def _uniquePaths(self, m, n):
        dp = [1]*n  # 第一行第一列都是一种走法
        for row in range(1, m):
            for col in range(1, n):
                # 等号右边，dp[n]是上一行该列走法，dp[n-1]是该行左边走法
                dp[col] = dp[col] + dp[col-1]
        return dp[n-1]
if __name__ == '__main__':
    obj = Solution()
    while True:
        m = int(input().strip())
        n = int(input().strip())
        res = obj._uniquePaths(m, n)
        print(res)