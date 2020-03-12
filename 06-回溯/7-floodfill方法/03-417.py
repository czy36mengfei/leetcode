# 太平洋大西洋水流问题
class Solution(object):
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    pacific = None
    atlantic = None
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n_row = len(matrix)
        if n_row == 0:
            return []
        n_col = len(matrix[0])
        self.pacific = [[False for _ in range(n_col)] for _ in range(n_row)]
        self.atlantic = [[False for _ in range(n_col)] for _ in range(n_row)]

        visited = [[False for _ in range(n_col)] for _ in range(n_row)]
        # 太平洋倒流
        for x in range(n_col):
            if visited[0][x] is False:
                self._dfs(matrix, x, 0, visited, n_row, n_col, is_pacific=True)

        for y in range(n_row):
            if visited[y][0] is False:
                self._dfs(matrix, 0, y, visited, n_row, n_col, is_pacific=True)

        visited = [[False for _ in range(n_col)] for _ in range(n_row)]
        # 大西洋倒流
        for x in range(n_col):
            if visited[n_row-1][x] is False:
                self._dfs(matrix, x, n_row-1, visited, n_row, n_col, is_pacific=False)

        for y in range(n_row):
            if visited[y][n_col-1] is False:
                self._dfs(matrix, n_col-1, y, visited, n_row, n_col, is_pacific=False)

        # 找出交汇点
        res = []
        for y in range(n_row):
            for x in range(n_col):
                if self.pacific[y][x] is True and self.atlantic[y][x] is True:
                    res.append([y, x])
        return res



    def _dfs(self, matrix, x, y, visited, n_row, n_col, is_pacific):
        # 倒流情况
        if is_pacific:
            self.pacific[y][x] = True
        else:
            self.atlantic[y][x] = True
        visited[y][x] = True
        # 二维回溯
        for d in self.direction:
            new_x = x + d[0]
            new_y = y + d[1]
            if 0 <= new_x < n_col and 0 <= new_y < n_row and \
                matrix[new_y][new_x] >= matrix[y][x] and visited[new_y][new_x] is False:
                self._dfs(matrix, new_x, new_y, visited, n_row, n_col, is_pacific)




