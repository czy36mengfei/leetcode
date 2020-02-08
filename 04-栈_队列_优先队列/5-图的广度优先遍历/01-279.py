# 图的广度优先搜索


class Solution(object):
    def numSquares(self, n):
        queue = [(0, n)]
        visited = [False for _ in range(n+1)]
        while queue:
            level, v = queue.pop(0)
            for i in range(n):

                last = v - i * i

                if last == 0:
                    return level+1
                elif last < 0:
                    break
                else:
                    if visited[last] is False:
                        queue.append((level+1, last))
                        visited[last] = True

if __name__ == '__main__':
    obj = Solution()
    while True:
        n = int(input().strip())
        res = obj.numSquares(n)
        print(res)


