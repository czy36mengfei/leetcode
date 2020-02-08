class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        length = len(prerequisites)
        if length == 0:
            return [i for i in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]
        adjacency = [set() for _ in range(numCourses)]
        # 获取入度表和邻接矩阵
        for cur, pre in prerequisites:
            in_degree[cur] += 1
            adjacency[pre].add(cur)

        # 零入度队列
        res = []
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        num = 0
        # 依次取0入度的
        while queue:
            top = queue.pop(0)
            res.append(top)
            num += 1
            for ad in adjacency[top]:
                in_degree[ad] -= 1
                if in_degree[ad] == 0:
                    queue.append(ad)
        if num == numCourses:
            return res
        else:
            return []

    def _findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        length = len(prerequisites)
        if length == 0:
            return [i for i in range(numCourses)]
        # 使用逆邻接矩阵
        inverse_adj = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            inverse_adj[cur].append(pre)
        # 0-未访问，1-正在访问，2-已访问（共同祖先）。
        # 不能出现1，不然就是环
        visited = [0 for _ in range(numCourses)]
        res = []
        for i in range(numCourses):
            # 存在环 dfs为True
            if self._dfs(inverse_adj, i, visited, res):
                return []
        return res

    def _dfs(self, inverse_adj, index, visited, res):
        # 终止条件
        if visited[index] == 1:
            return True
        if visited[index] == 2:
            return False

        visited[index] = 1
        for pre in inverse_adj[index]:
            if self._dfs(inverse_adj, pre, visited, res):
                return True
        visited[index] = 2
        res.append(index)
        return False
