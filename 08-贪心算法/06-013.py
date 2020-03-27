class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        if length == 0:
            return 0
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = roman_dict[s[0]]
        for i in range(1, length):
            if roman_dict[s[i]] > roman_dict[s[i-1]]:
                # 之前的那个数比较小
                # 扣掉原来加的，在扣掉它对现在数的减效应
                res += roman_dict[s[i]] - 2*roman_dict[s[i-1]]
            else:
                res += roman_dict[s[i]]
        return res
