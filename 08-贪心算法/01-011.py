class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 2:
            return 0
        res = 0

        left = 0
        right = length-1
        while left < right:
            water = (right-left) * min(height[left], height[right])
            res = max(res, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


