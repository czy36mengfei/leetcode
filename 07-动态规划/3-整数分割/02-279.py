# 动态规划，整数划分
import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0] * (n+1)
        for i in range(1, n+1):
            res = sys.maxsize
            j = 1
            while i - j * j >= 0:
                res = min(res, 1 + nums[i-j*j])
                j += 1
            nums[i] = res
        return nums[n]
    def _numSquares(self, n):
        visited = [False for _ in range(n)]
        queue = [(0, n)]
        while queue:
            level, top = queue.pop(0)
            level += 1  # 新的子节点是父节点的下一层
            i = 1
            while True:
                last = top - i * i
                if last == 0:
                    return level
                elif last < 0:
                    break
                else:
                    if visited[last] is False:
                        queue.append((level, last))
                        visited[last] = True
                i += 1


if __name__ == '__main__':
    obj = Solution()
    while True:
        n = int(input().strip())
        res = obj._numSquares(n)
        print(res)



