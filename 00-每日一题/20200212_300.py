# 最长上升子序列
"""
关键：找大于等于“当前遍历的那个数”的第 1 个索引，将它替换成“当前遍历的那个数”，这样使得这个数变小，后面才有可能接一个更大的数。

注意：辅助数组不一定是一个最长上升子序列，但辅助数组的长度一定是最长上升子序列的长度。
"""

# 替换掉第一个大于等于自己的，那么不会对已有最长子序列产生影响，因为比这个大的还是会排在这个后面，该延长还是会延长
# 而这个又更新了久的，可以构造新的子序列

class Solution:
    def lengthOfLIS(self, nums):

        size = len(nums)
        if size < 2:
            return size

        tail = []

        for num in nums:
            length = len(tail)
            l = 0
            r = length
            if length == 0:
                tail.append(num)
                continue

            while l < r:

                mid = (l+r) // 2  # 左边界
                if tail[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            if l == len(tail):
                tail.append(num)
            else:
                tail[l] = num

        return len(tail)

if __name__ == '__main__':

    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.lengthOfLIS(nums)
        print(res)

