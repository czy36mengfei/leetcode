class Solution:
    def twoSum(self, numbers, target):

        length = len(numbers)
        if length < 2:
            return []
        left = 0
        right = length-1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return []
if __name__ == '__main__':

    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        target = int(input().strip())
        res = obj.twoSum(nums, target)
        print(res)
