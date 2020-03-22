class Solution:
    def __init__(self):
        self.cache = []

    def _best_value(self, weights, values, index, capacity):
        # 临界问题
        if index < 0 or capacity < 0:
            return 0
        if self.cache[index][capacity] != -1:
            return self.cache[index][capacity]

        # 该值不取，只取前面的情况
        res = self._best_value(weights, values, index-1, capacity)
        if weights[index] <= capacity:  # 该物体可以取
            res = max(res, values[index]+self._best_value(weights, values, index-1, capacity-weights[index]))
        self.cache[index][capacity] = res
        return res
    def knapscak01(self, weights, values, C):
        l = len(weights)
        if l == 0:
            return 0
        self.cache = [[-1 for _ in range(C+1)] for _ in range(l)]
        return self._best_value(weights, values, l-1, C)