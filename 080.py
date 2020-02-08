# 既然可以重复2个，那么不同的数就放在对比的数后移2为的位置，前提，放的位置之前的都已经放了

class Solution(object):
    def removeDuplicates(self, nums):
        length = len(nums)

        if length < 2:
            return length

        j = 1

        for i in range(2, length):
            if nums[i] != nums[j-1]:
                j = j+1
                nums[j] = nums[i]

        return j + 1

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.removeDuplicates(nums)
        print(res)

