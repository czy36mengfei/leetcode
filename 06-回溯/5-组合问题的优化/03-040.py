
# 在一个for 循环里决策是同一位，所以同样的字母不必重复尝试

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        res = []
        # 排序，使其可以用递归
        candidates = sorted(candidates)
        self._dfs(candidates, 0, target, [], res)
        return res
    def _dfs(self, candidates, start, last, pre, res):

        if last < 0:
            return
        if last == 0:
            res.append(pre[:])
            return

        for i in range(start, len(candidates)):
            # 剪枝-不可能分支
            if last - candidates[i] < 0:
                break
            # 剪枝-重复分支
            if i > start and candidates[i] == candidates[i-1]:
                # 在同一个循环里决策的是同一位，i>start,说明前一个已经试过了
                # 此时当前与前一个相同，就没必要在试一次
                continue

            pre.append(candidates[i])
            # 一个数只能用一次，就得从下一个开始（可重复就从当前）
            self._dfs(candidates, i+1, last-candidates[i], pre, res)
            # 回溯
            pre.pop()




if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        target = int(input().strip())
        res = obj.combinationSum2(nums, target)
        print(res)