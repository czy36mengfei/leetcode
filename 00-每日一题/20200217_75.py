# 三路快排
class Solution:
    def sortColors(self, nums):
        length = len(nums)
        # 三部分， 2条线
        first = -1
        second = length
        i = 0
        while i < second:

            if nums[i] == 0:
                first += 1
                nums[first], nums[i] = nums[i], nums[first]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                second -= 1
                nums[second], nums[i] = nums[i], nums[second]
                # 换过来的不知道，所以这边不能懂，要继续判断

        return nums

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.sortColors(nums)
        print(res)