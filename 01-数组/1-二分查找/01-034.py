# 在排序数组查找元素第一个和最后一个位置
class Solution:
    def searchRange(self, nums, target):

        left = self.find_left(nums, target)
        if left == -1:
            return [-1, -1]

        right = self.find_right(nums, target)

        return [left, right]


    def find_left(self, nums, target):
        lenght =len(nums)
        if lenght == 0:
            return -1
        l = 0
        r = lenght -1
        while l < r:
            mid = (l + r) // 2  # 2个的时候，左边是左边界
            if nums[mid] < target:
                l = mid + 1  # 左边只会小的时候前移，所以一直截这左边界
            else:
                r = mid
        if nums[l] == target:
            return l
        else:
            return -1

    def find_right(self, nums, target):
        lenght = len(nums)
        if lenght == 0:
            return -1
        l = 0
        r = lenght - 1
        while l < r:
            mid = (l + r) // 2 + 1  # 2个的时候，右边边是右边界
            if nums[mid] > target:
                r = mid - 1  # 右边边只会大的时候左移，所以一直截这右边界
            else:
                l = mid
        if nums[r] == target:
            return r
        else:
            return -1

if __name__ == '__main__':
    obj = Solution()

    while 1:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        target = int(input().strip())
        res = obj.searchRange(nums, target)
        print(res)