# 对撞指针
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        length = len(s)
        left = 0
        right = length - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)


if __name__ == '__main__':

    obj = Solution()
    while True:
        s = input().strip()
        res = obj.reverseVowels(s)
        print(res)