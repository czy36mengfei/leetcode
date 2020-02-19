# 215. 数组中的第 K 个最大元素
# 在未排序的数组中找到第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
import heapq
class Solution:

    # 数组中的第 K 个最大元素
    # 数组中第 k 大的元素，它的索引是 len(nums) - k

    def _findKthLargest(self, nums, k):

        L = []
        for i in range(k):
            heapq.heappush(L, nums[i])
        for j in range(k, len(nums)):
            if nums[j] > L[0]:
                heapq.heapreplace(L, nums[j])


        return L[0]


    def findKthLargest(self, nums, k):

        length = len(nums)
        # if k > length:
        #     return 'error'
        left = 0
        right = length - 1

        while True:
            index = self.partition(nums, left, right)
            if index == length - k:
                return nums[index]

            elif index < length - k:  #  第k大的数在后面的区间
                left = index+1
            else:
                right = index-1



    def partition(self, nums, left, right):
        """返回第一个数是第几小的，并把比它小的放到前面"""

        first_value = nums[left]
        j = left

        for i in range(left+1, right+1):
            if nums[i] < first_value:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[j], nums[left] = nums[left], nums[j]
        return j

if __name__ == '__main__':

    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        k = int(input().strip())
        res = obj.findKthLargest(nums, k)
        print(res)
