# 被围绕的区域
# 找出边界区域，其他的就是被围绕区域
class Solution(object):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n_row = len(board)
        if n_row == 0:
            return board
        n_col = len(board[0])
        for y in [0,n_row-1]:
            for x in range(n_col):
                if board[y][x] == 'O':
                    self._dfs(board, x, y, n_row, n_col)

        for x in [0, n_col-1]:
            for y in range(n_row):
                if board[y][x] == 'O':
                    self._dfs(board, x, y, n_row, n_col)

        # 把里面的O替换为X
        # 把外围的-替换回O

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'
        return board



    def _dfs(self, board, x, y, n_row, n_col):
        board[y][x] = '-'
        for d in self.direction:
            new_x = x + d[0]
            new_y = y + d[1]

            if 0 <= new_x < n_col and 0 <= new_y < n_row and board[new_y][new_x]=='O':
                self._dfs(board, new_x, new_y, n_row, n_col)





if __name__ == '__main__':
    obj = Solution()
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    res = obj.solve(board)
    print(res)