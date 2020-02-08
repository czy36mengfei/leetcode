# 想一个办法把2个数分在不同组，
# 和他同组的每个数都有2个，异或还是会得到0
class Solution(object):
    def findNumsAppearOnce(self, nums):
        if len(nums) == 2:
            return nums

        xor = 0
        for num in nums:
            xor = xor ^ num

        # 异或结构找出右数的一个为以的点，则是2数不同所在，可以将2数分组

        i = 0
        while xor & 1 == 0:
            xor = xor >> 1
            i += 1

        res1 = 0
        res2 = 0
        for num in nums:
            # 分为2组，两个数在不同组中
            if (num >> i) & 1 == 1:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]

if __name__ == '__main__':
    obj = Solution()
    nums = [3, 2, 6, 4, 2, 5, 6, 5, 0, 0, 1, 4]
    res = obj.findNumsAppearOnce(nums)
    print(res)