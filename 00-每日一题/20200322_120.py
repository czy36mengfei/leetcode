class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        if length == 0:
            return 0
        dp = [v for v in triangle[-1]]

        for i in range(length-2,-1,-1):
            row_len = len(triangle[i])
            for j in range(row_len):
                # 看下方两侧哪个小
                dp[j] = min(triangle[i][j]+dp[j], triangle[i][j]+dp[j+1])
        return dp[0]





