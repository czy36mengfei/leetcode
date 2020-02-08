# 全排列
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0:
            return []
        res = []
        visited = [False for _ in range(length)]
        self._permute(nums, length, [], visited, res)
        return res

    def _permute(self, nums, length, pre, visited, res):

        if len(pre) == length:
            res.append(pre.copy())
            return

        for i in range(length):
            if visited[i] is False:
                visited[i] = True
                pre.append(nums[i])
                self._permute(nums, length, pre, visited, res)
                pre.pop()
                visited[i] = False

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.permute(nums)
        print(res)



