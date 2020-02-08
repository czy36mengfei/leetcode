
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pre_str = {}
        max_len = 0
        start = 0

        for i, c in enumerate(s):
            if c in pre_str:
                start = max(start, pre_str[c]+1)
            pre_str[c] = i
            max_len = max(max_len, i-start+1)
        return max_len


if __name__ == '__main__':

    obj = Solution()
    while True:
        s = input()
        res = obj.lengthOfLongestSubstring(s)
        print(res)

