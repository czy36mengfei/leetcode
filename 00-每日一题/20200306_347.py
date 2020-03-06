# 前k个高频元素
import heapq
import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1
        queue = []
        for key in counts:
            heapq.heappush(queue, (-counts[key], key))
        res = []
        for _ in range(k):
            _, word = heapq.heappop(queue)
            res.append(word)
        return res


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        k = int(input())
        res = obj.topKFrequent(nums, k)
        print(res)



