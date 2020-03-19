class Solution(object):

    # 定义移动方向
    direction = [(0,-1),(0,1),(-1,0),(1,0)]
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n_row = len(board)
        n_col = len(board[0])
        visited = [[False for _ in range(n_col)] for _ in range(n_row)]
        if n_row == 0 or n_col==0:
            return False
        for i in range(n_row):
            for j in range(n_col):
                if self._search(board, word, 0, i, j, visited, n_row, n_col):
                    return True
        return False


    def _search(self, board, word, index, start_x, start_y, visited, n_row, n_col):
        #  终止条件
        if index == len(word)-1:
            return board[start_x][start_y] == word[-1]

        if board[start_x][start_y] == word[index]:
            visited[start_x][start_y] = True
            for d in self.direction:
                new_x = start_x + d[0]
                new_y = start_y + d[1]
                if 0<= new_x < n_row and 0<= new_y < n_col \
                    and visited[new_x][new_y] is False \
                    and self._search(board, word, index+1, new_x,new_y,visited,n_row,n_col):
                    return True
            visited[start_x][start_y] = False
        return False





