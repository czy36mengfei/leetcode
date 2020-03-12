class Solution(object):
    col = None
    dia = None
    dia_back = None
    res = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """


        if n == 0:
            return 0

        self.col = [False for _ in range(n)]
        # 对角线
        # 正对角线 \
        # 两数坐标之和从0到2n-2
        self.dia = [False for _ in range(2 * n - 1)]
        # 反对角线 /
        # 两数坐标只差由-n+1到n-1
        # 加上n-1后，可定位至0到2n-2
        self.dia_back = [False for _ in range(2 * n - 1)]
        self.res = 0
        self._dfs(n, 0, [])
        return self.res



    def _dfs(self, n, row, pre):
        # 回溯结束
        if row == n:
            self.res += 1
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

                self._dfs(n, row+1, pre)

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
