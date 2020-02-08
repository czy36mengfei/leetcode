class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        length = len(prerequisites)
        if length <= 1:
            return True
        in_degree = [0 for _ in range(numCourses)]
        adjacency = [set() for _ in range(numCourses)]
        # 获取入度表和邻接矩阵
        for cur, pre in prerequisites:
            in_degree[cur] += 1
            adjacency[pre].add(cur)

        # 零入度队列
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        num = 0
        # 依次取0入度的
        while queue:
            top = queue.pop(0)
            num += 1
            for ad in adjacency[top]:
                in_degree[ad] -= 1
                if in_degree[ad] == 0:
                    queue.append(ad)
        if num == numCourses:
            return True
        else:
            return False

    def _canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        length = len(prerequisites)
        if length <= 1:
            return True
        # 使用逆邻接矩阵
        inverse_adj = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            inverse_adj[cur].append(pre)
        # 0-未访问，1-正在访问，2-已访问（共同祖先）。
        # 不能出现1，不然就是环
        visited = [0 for _ in range(numCourses)]

        for i in range(numCourses):
            # 存在环 dfs为True
            if self._dfs(inverse_adj, i, visited):
                return False
        return True

    def _dfs(self, inverse_adj, index, visited):
        # 终止条件
        if visited[index] == 1:
            return True
        if visited[index] == 2:
            return False

        visited[index] = 1
        for pre in inverse_adj[index]:
            if self._dfs(inverse_adj, pre, visited):
                return True
        visited[index] = 2
        return False
