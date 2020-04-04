class Solution(object):
    class FenwickTree():
        def __init__(self, size):
            self.size = size
            self.father = [0 for _ in range(self.size+1)]

        def _lowbit(self, x):
            return x & (-x)

        def update(self, index, delta):
            while index <= self.size:
                self.father[index] += delta
                index += self._lowbit(index)

        def query(self, index):
            res = 0
            while index > 0:
                res += self.father[index]
                index -= self._lowbit(index)
            return res

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return []
        if length == 1:
            return [0]
        rank_num = set(nums)
        rank_num = sorted(rank_num)
        rank_map = dict()
        for i, num in enumerate(rank_num):
            rank_map[num] = i+1

        ft= Solution.FenwickTree(len(rank_num))

        # 从后往前填表
        res = [None for _ in range(length)]
        for i in range(length-1, -1, -1):
            rank = rank_map[nums[i]]
            ft.update(rank, 1)
            res[i] = ft.query(rank-1)
        return res



if __name__ == '__main__':
    obj = Solution()
    nums = [5,2,6,1]
    res = obj.countSmaller(nums)
    print(res)