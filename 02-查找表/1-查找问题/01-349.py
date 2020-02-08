class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = list({n for n in nums1 if n in nums2})
        return res


if __name__ == '__main__':

    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        nums2_str = input().strip().split()
        nums2 = list(map(int, nums2_str))
        res = obj.intersection(nums, nums2)
        print(res)