# 动态规划  整数分割
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 1
        product = [0] * (n+1)
        product[1] = 1
        for i in range(2, n+1):
            max_product = 0
            for j in range(1, i):
                max_product = max(max_product, j * product[i-j], j * (i-j))  # 只要一侧逼近就好，它们是等价的。只要一侧分解就可以，另一侧分解可以在之前的情况中找到
            product[i] = max_product

        return product[n]

if __name__ == '__main__':
    obj = Solution()
    while True:
        n = int(input().strip())
        res = obj.integerBreak(n)
        print(res)