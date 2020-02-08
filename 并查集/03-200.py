class Solution(object):

    father = []
    m = 0
    count = 0

    def find(self, q):
        if self.father[q] != q:
            self.father[q] = self.find(self.father[q])
        return self.father[q]
    def union(self, q, p):
        root_q = self.find(q)
        root_p = self.find(p)
        if root_p == root_q:
            return
        self.count -= 1
        self.father[root_q] = root_p
    def is_connected(self, q, p):
        root_q = self.find(q)
        root_p = self.find(p)
        return root_p == root_q

    def get_index(self, i, j):
        return self.m * i + j

    def numIslands(self, grid):

        n = len(grid)
        if n == 0:
            return 0
        self.m = len(grid[0])

        for i in range(n):
            for j in range(self.m):
                if grid[i][j] == '1':
                    self.count += 1

        self.father = [i for i in range(n*self.m)]

        for i in range(n):
            for j in range(self.m):
                if grid[i][j] == '1':
                    if i < n-1 and grid[i+1][j] == '1':
                        self.union(self.get_index(i, j), self.get_index(i + 1, j))
                    if j < self.m-1 and grid[i][j+1] == '1':
                        self.union(self.get_index(i, j), self.get_index(i, j + 1))

        return self.count

if __name__ == '__main__':
    obj = Solution()
    grid =[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    res = obj.numIslands(grid)
    print(res)

