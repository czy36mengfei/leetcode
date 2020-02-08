# 搜索插入位置
class Solution:
    def searchInsert(self, nums, target):

        length = len(nums)
        if length == 0:
            return 0

        # 找左边界的思想
        l = 0
        r = length  # 包含在最左端的前馈

        while l < r:
            mid = (l + r) // 2  # 两个的时候取左
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        target = int(input().strip())
        res = obj.searchInsert(nums, target)
        print(res)
