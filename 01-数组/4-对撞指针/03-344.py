# 对撞指针
class Solution(object):

    def reverseString(self, s):
        length = len(s)
        if length < 2:
            return s

        left = 0
        right = length - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

if __name__ == '__main__':
    if __name__ == '__main__':

        obj = Solution()
        while True:
            s = list(input().strip())
            res = obj.reverseString(s)
            print(res)