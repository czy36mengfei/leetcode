class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}
        for n in nums1:
            count[n] = count.get(n, 0) + 1

        result = []
        for n in nums2:
            if n in count and count[n] > 0:
                result.append(n)
            count[n] = count.get(n, 0) - 1
        return result

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        nums_str2 = input().strip().split()
        nums2 = list(map(int, nums_str2))

        res = obj.intersect(nums, nums2)
        print(res)
