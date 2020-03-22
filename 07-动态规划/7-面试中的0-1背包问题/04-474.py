class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for s in strs:
            # 计算该字符的01数
            num_0 = 0
            num_1 = 0
            for c in s:
                if c =='0':
                    num_0 +=1
                else:
                    num_1 +=1

            # 判断当前字符下的二维背包
            for i in range(m, -1, -1):  # 逆序，每次使用的都是位置比较小的，是上个字符串的结果
                for j in range(n, -1, -1):  # 可能只有0，或1，另一个是0个
                    if i-num_0 >=0 and j-num_1>=0:
                        dp[i][j] = max(dp[i][j], 1+dp[i-num_0][j-num_1])  # 取与不取字符串，选最大
        return dp[-1][-1]


if __name__ == '__main__':
    obj = Solution()
    while True:
        strs = input().strip().split()
        m = int(input().strip())
        n = int(input().strip())
        res = obj.findMaxForm(strs, m, n)
        print(res)
