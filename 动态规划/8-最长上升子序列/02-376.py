class Solution(object):

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return length

        up = 1
        down = 1
        for i in range(1, length):
            if nums[i-1] < nums[i]:
                # 上升
                up = down + 1
            elif nums[i-1] > nums[i]:
                # 下降
                down = up + 1
        return max(up, down)


if __name__ == '__main__':
    obj = Solution()
    while True:
        nums_str = input().strip().split()
        nums = list(map(int, nums_str))
        res = obj.wiggleMaxLength(nums)
        print(res)
