class Solution(object):
    count = 0
    parent = []
    def find(self, q):
        if q != self.parent[q]:
            self.parent[q] = self.find(self.parent[q])
        return self.parent[q]
    def union(self, q, p):
        root_q = self.find(q)
        root_p = self.find(p)

        if root_q == root_p:
            return
        else:
            self.parent[root_p] = root_q
            self.count -= 1


    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        self.count = n
        self.parent = [i for i in range(n)]

        for i in range(n):
            for j in range(i):  # 左下三角，且没有对角线
                if M[i][j] == 1:
                    self.union(i, j)

        return self.count
