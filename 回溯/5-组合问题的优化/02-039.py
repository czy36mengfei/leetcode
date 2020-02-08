class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        res = []
        candidates = sorted(candidates)
        self._dfs(candidates, 0, target, [], res)
        return res


    def _dfs(self, candidates, start, last, pre, res):
        if last < 0:
            return
        if last == 0:  # last是剩余
            res.append(pre[:])
        length = len(candidates)
        for i in range(start, length):
            # 剪枝
            if i < last-candidates[i] < 0:
                break
            pre.append(candidates[i])
            # 可以重复使用，所以下一个也从i开始
            self._dfs(candidates, i, last-candidates[i], pre, res)
            pre.pop()  # 回溯




if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        target = int(input().strip())
        res = obj.combinationSum(nums, target)
        print(res)