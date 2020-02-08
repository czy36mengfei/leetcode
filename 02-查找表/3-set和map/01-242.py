from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_c = Counter(s)
        t_c = Counter(t)
        if s_c == t_c:
            return True
        else:
            return False
if __name__ == '__main__':
    obj = Solution()
    while True:
        s = input().strip()
        # nums = list(map(int, nums_str))
        t = input().strip()
        # nums2 = list(map(int, nums_str2))

        res = obj.isAnagram(s, t)
        print(res)
