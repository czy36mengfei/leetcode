class Solution(object):
    row_used = None
    col_used = None
    box_used = None
    n = 9
    size = 3

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        self.row_used = [[False for _ in range(10)] for _ in range(self.n)]
        self.col_used = [[False for _ in range(10)] for _ in range(self.n)]
        self.box_used = [[False for _ in range(10)] for _ in range(self.n)]
        # 初始化
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] != '.':
                    num = int(board[i][j])

                    self.row_used[i][num] = True
                    self.col_used[j][num] = True
                    self.box_used[i // self.size * self.size + j // self.size][num] = True
        self._dfs(board, 0, 0)

    def _dfs(self, board, i, j):
        if j == self.n:
            i += 1
            j = 0
            if i == self.n:
                return True


        if board[i][j] == '.':
            # 尝试填充0-9
            for d in range(1, 10):
                can_use = (self.row_used[i][d] is False and self.col_used[j][d] is False and
                           self.box_used[i // self.size * self.size + j // self.size][d] is False)
                if can_use:
                    # 遍历当前格
                    board[i][j] = str(d)
                    self.row_used[i][d] = True
                    self.col_used[j][d] = True
                    self.box_used[i // self.size * self.size + j // self.size][d] = True

                    # 继续遍历下一个
                    if self._dfs(board, i, j + 1):
                        return True
                    # 回溯
                    board[i][j] = '.'
                    self.row_used[i][d] = False
                    self.col_used[j][d] = False
                    self.box_used[i // self.size * self.size + j // self.size][d] = False
        else:
            # 直接遍历下一个
            return self._dfs(board, i, j + 1)
        return False
if __name__ == '__main__':
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    solution = Solution()
    solution.solveSudoku(board)

    for row in board:
        print(row)