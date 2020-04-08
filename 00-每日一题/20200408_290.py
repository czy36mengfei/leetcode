# 查找表
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        n_patt = len(pattern)
        s_list = str.split(' ')
        n_s = len(s_list)
        if n_patt != n_s:
            return False
        ps_map = dict()
        pattern_set = set()
        for i in range(n_patt):
            if s_list[i] not in ps_map:
                if pattern[i] in pattern_set:
                    return False  # 使用了相同的pattern
                ps_map[s_list[i]] = pattern[i]
                pattern_set.add(pattern[i])
            else:
                if ps_map[s_list[i]] != pattern[i]:
                    return False
        return True


if __name__ == '__main__':
    obj = Solution()
    while True:
        pattern = input().strip()
        s = input().strip()
        res = obj.wordPattern(pattern, s)
        print(res)