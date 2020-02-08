# 删除重复项
class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        j = 0

        for i in range(1, length):
            if nums[i] != nums[j]:  # 有不重复项，就往前移
                j += 1
                nums[j] = nums[i]
        return j+1

if __name__ == '__main__':
    obj = Solution()

    while 1:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.removeDuplicates(nums)
        print(res)



