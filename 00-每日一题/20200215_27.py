# 移除元素
class Solution:
    def removeElement(self, nums, val):

        j = 0

        for num in nums:
            if num == val:
                continue
            else:
                nums[j] = num
                j += 1
        return j


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        val = int(input().strip())

        res = obj.removeElement(nums, val)
        print(res)