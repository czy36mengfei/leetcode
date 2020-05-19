class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self._dfs(s, 0, [], res)
        return res

    def is_huiwen(self, s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def _dfs(self, s, start, pre, res):

        if start == len(s):
            res.append(pre[:])
            return

        for i in range(start, len(s)):
            seg = s[start:i+1]
            if self.is_huiwen(seg):
                pre.append(seg)
                self._dfs(s, i+1, pre, res)
                pre.pop()


if __name__ == '__main__':
    obj = Solution()
    print(obj.is_huiwen('bbab'))
    while True:
        s = input().strip()
        res = obj.partition(s)
        print(res)