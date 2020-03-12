class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0:
            return [[]]

        res = []
        nums = sorted(nums)
        for max_len in range(0, length+1):
            self._dfs(nums, 0, max_len, [], res)
        return res

    def _dfs(self, nums, start, max_len, pre, res):
        if len(pre) == max_len:
            res.append(pre[:])
            return

        for i in range(start, len(nums)):
            # 同一个位置的替换不必要考虑重复的元素
            if i > start and nums[i] == nums[i-1]:
                continue
            pre.append(nums[i])
            self._dfs(nums, i+1, max_len, pre, res)
            pre.pop()


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.subsetsWithDup(nums)
        print(res)
