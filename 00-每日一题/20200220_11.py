# 对撞指针
# 固定一端， 高的往里面走，只会容积变小， 短在高不变，宽有减小

class Solution:
    def maxArea(self, height):
        length = len(height)
        left = 0
        right = length-1
        res = 0
        while left < right:
            min_side = min(height[left], height[right])
            res = max(res, min_side * (right-left))
            if min_side == height[left]:
                left += 1
            else:
                right -= 1

        return res

if __name__ == '__main__':

    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.maxArea(nums)
        print(res)