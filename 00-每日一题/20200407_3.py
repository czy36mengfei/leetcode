import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        c_dict = collections.defaultdict(int)
        max_len = 0
        s_len = len(s)
        if s_len < 2:
            return s_len

        while right < s_len:

            if c_dict[s[right]] <= 0:
                c_dict[s[right]] += 1
                right += 1

            else:
                c_dict[s[left]] -= 1
                left += 1

            if right-left > max_len:
                max_len = right-left

        return max_len


if __name__ == '__main__':

    obj = Solution()
    while True:
        s = input()
        res = obj.lengthOfLongestSubstring(s)
        print(res)
