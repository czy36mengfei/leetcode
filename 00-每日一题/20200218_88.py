class Solution:
    def merge(self, nums1, m, nums2, n):

        m_j = m - 1
        n_j = n - 1

        for i in range(n + m - 1, -1, -1):

            if m_j < 0:
                nums1[i] = nums2[n_j]
                n_j -= 1
            elif n_j < 0:
                nums1[i] = nums1[m_j]
                m_j -= 1
            elif nums1[m_j] > nums2[n_j]:
                nums1[i] = nums1[m_j]
                m_j -= 1
            else:
                nums1[i] = nums2[n_j]
                n_j -= 1
        return nums1

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums1_str = input().strip().split()
        nums1 = list(map(int, nums1_str))
        m = 0
        for nums in nums1:
            if nums != 0:
                m += 1

        nums2_str = input().strip().split()
        nums2 = list(map(int, nums2_str))
        n = len(nums2)

        res = obj.merge(nums1, m, nums2, n)
        print(res)