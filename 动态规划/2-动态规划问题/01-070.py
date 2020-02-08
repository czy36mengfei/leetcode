# 爬楼梯
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n >=1
        memory = [0 for _ in range(n+1)]
        memory[0] = 1
        memory[1] = 1
        for i in range(2, n+1):
            memory[i] = memory[i-1] + memory[i-2]
        return memory[n]

if __name__ == '__main__':
    while True:
        obj = Solution()
        n = int(input())
        res = obj.climbStairs(n)
        print(res)