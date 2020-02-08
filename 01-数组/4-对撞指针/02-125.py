# 对撞指针
class Solution(object):
    def isPalindrome(self, s):
        length = len(s)
        if length == 0:
            return True

        left = 0
        right = length - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

if __name__ == '__main__':

    obj = Solution()
    while True:
        s = input().strip()
        res = obj.isPalindrome(s)

        print(res)
