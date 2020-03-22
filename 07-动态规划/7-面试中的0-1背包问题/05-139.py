class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        dp = [False for _ in range(length+1)]
        dp[0] = True

        for i in range(1, length+1):
            for j in range(i):   # 用来截取后半部分
                # dp[j]是从0开始的字符肯定在之前判断了
                # s[j:i] 截取的是后半段, 第i就是前面几个字符串。i=5，就是[0:5],5个字符的字符串
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]

if __name__ == '__main__':
    obj = Solution()
    while True:
        s = input().strip()
        word_dict = input().strip().split()

        res = obj.wordBreak(s, word_dict)
        print(res)