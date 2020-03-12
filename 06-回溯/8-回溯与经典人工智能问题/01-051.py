class Solution(object):
    col = None
    dia = None
    dia_back = None

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        res = []
        if n == 0:
            return []

        self.col = [False for _ in range(n)]
        # 对角线
        # 正对角线 \
        # 两数坐标之和从0到2n-2
        self.dia = [False for _ in range(2 * n - 1)]
        # 反对角线 /
        # 两数坐标只差由-n+1到n-1
        # 加上n-1后，可定位至0到2n-2
        self.dia_back = [False for _ in range(2 * n - 1)]
        self._dfs(n, 0, [], res)
        return res


    def draw_res(self, lists):
        res = []
        for q in lists:
            line = ''
            for i in range(len(lists)):
                if i != q:
                    line += '.'
                else:
                    line += 'Q'
            res.append(line)

        return res

    def _dfs(self, n, row, pre, res):
        # 回溯结束
        if row == n:
            res.append(self.draw_res(pre))
            return

        # 遍历
        for i in range(n):
            if self.col[i] is False and self.dia[i + row] is False \
                    and self.dia_back[i - row + n - 1] is False:
                # 状态设置
                self.col[i] = True
                self.dia[i + row] = True
                self.dia_back[i - row + n - 1] = True
                pre.append(i)

                self._dfs(n, row+1, pre, res)

                # 回溯，清除状态
                self.col[i] = False
                self.dia[i + row] = False
                self.dia_back[i - row + n - 1] = False
                pre.pop()

if __name__ == '__main__':
    obj = Solution()
    while True:
        n = int(input())
        res = obj.solveNQueens(n)
        print(res)
