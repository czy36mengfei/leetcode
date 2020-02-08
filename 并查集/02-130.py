# 被围绕的区域
class Solution(object):
    # 因为从左到右，从上到下，所以只需考虑下或右是否连通
    parent = []
    m = 0
    # direction = [(1, 0), (0, 1)]

    def find(self, q):
        if self.parent[q] != q:
            self.parent[q] = self.find(self.parent[q])
        return self.parent[q]

    def union(self, q, p):
        root_q = self.find(q)
        root_p = self.find(p)
        if root_q == root_p:
            return
        self.parent[root_p] = root_q

    def is_connected(self, q, p):
        root_q = self.find(q)
        root_p = self.find(p)
        return root_q == root_p

    def get_index(self, i, j):
        return i * self.m + j

    def solve(self, board):

        n = len(board)

        if n == 0:
            return board
        m = len(board[0])
        self.m = m
        self.parent = [i for i in range(n*m+1)]
        bound = n * m

        # 把边界作为一块
        for i in [0, n-1]:
            for j in range(m):
                self.union(self.get_index(i, j), bound)

        for j in [0, m-1]:
            for i in range(n):
                self.union(self.get_index(i, j), bound)

        # 小于等于2不可能围
        if n <= 2 or m <= 2:
            return board
        # 把相邻块连通
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] == 'O':
                    if board[i+1][j] == 'O':
                        self.union(self.get_index(i, j), self.get_index(i+1, j))
                    if board[i][j+1] == 'O':
                        self.union(self.get_index(i, j), self.get_index(i, j+1))

        for i in range(1, n-1):
            for j in range(1, m-1):
                if board[i][j] != 'O':
                    continue
                if self.is_connected(self.get_index(i,j), bound):
                    continue
                else:
                    board[i][j] = 'X'
        return board

if __name__ == '__main__':
    obj = Solution()
    board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
    res = obj.solve(board)
    print(res)
