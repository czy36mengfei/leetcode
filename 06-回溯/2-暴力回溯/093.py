
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return []
        res = []
        self._dfs(s, 0, 0, '', res)
        return res

    def is_addr(self, s):
        if len(s) > 1 and s.startswith('0'):
            return False
        return int(s) < 256

    def _dfs(self, s, start, split, pre, res):
        if split == 4:
            if start == len(s):
                res.append(pre[:-1])
            return

        for i in range(start, min(start+3, len(s))):
            # 切下来一段
            seg = s[start:i+1]
            if self.is_addr(seg):
                # 对余下的继续切段
                self._dfs(s, i+1, split+1, pre+seg+'.', res)



if __name__ == '__main__':
    obj = Solution()
    while True:
        s = input().strip()
        res = obj.restoreIpAddresses(s)
        print(res)


