class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        length = len(s)
        dp = [False for _ in range(length+1)]
        dp[0] = True

        for i in range(length+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True

        res = []
        if dp[-1]:
            self._dfs2(s, length, wordDict, dp, [], res)
        return res

    def _dfs(self, s, length, wordDict, dp, path, res):
        if length == 0:
            return res.append(' '.join(reversed(path)))
        for i in range(length):
            back_str = s[i:length]
            if back_str in wordDict and dp[i]:  # 两部分都在
                path.append(back_str)
                self._dfs(s, i, wordDict, dp, path, res)
                path.pop()
    def _dfs2(self, s, length, wordDict, dp, path, res):
        if length == 0:
            return res.append(' '.join(reversed(path)))
        for i in range(length-1,-1,-1):
            back_str = s[i:length]
            if back_str in wordDict and dp[i]:  # 两部分都在
                path.append(back_str)
                self._dfs(s, i, wordDict, dp, path, res)
                path.pop()


if __name__ == '__main__':
    obj = Solution()
    while True:
        s = input().strip()
        word_dict = input().strip().split()

        res = obj.wordBreak(s, word_dict)
        print(res)


"""
catsanddog
cat cats and sand dog
['cat sand dog', 'cats and dog']
pineapplepenapple
apple pen applepen pine pineapple
['pine applepen apple', 'pineapple pen apple', 'pine apple pen apple']
catsandog
cats dog sand and cat
[]

"""