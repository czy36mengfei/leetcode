class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]

        for i in range(1,m):
            for j in range(1, n):
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]

if __name__ == '__main__':
    obj = Solution()
    while True:
        m = int(input())
        grid = []
        for i in range(m):
            nums_str = input().strip().split()
            nums = list(map(int, nums_str))
            grid.append(nums)
        res = obj.minPathSum(grid)
        print(res)

