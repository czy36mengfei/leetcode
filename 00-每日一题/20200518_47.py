# 含重复数字的全排列
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        res = []
        nums = sorted(nums)
        visited = [False for _ in range(len(nums))]
        self._dfs(0, nums, [], visited, res)
        return res

    def _dfs(self, index, nums, pre, visited, res):

        if index == len(nums):
            res.append(pre.copy())
            return

        for i in range(len(nums)):
            if visited[i] is False:
                # nums[i-1] == nums[i] 当前遍历与上一个一样
                # visited[i-1] is False 当前遍历的pre没用上一个，所以不是补后面的，而是重复前一轮
                if i !=0 and nums[i-1] == nums[i] and visited[i-1] is False:
                    continue
                visited[i] = True
                pre.append(nums[i])
                self._dfs(index+1, nums, pre, visited, res)
                pre.pop()
                visited[i] = False


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.permuteUnique(nums)
        print(res)


