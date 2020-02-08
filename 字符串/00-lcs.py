# 最长公共子串和最长公共子序列
class Solution:
    # 最长公共子串
    def longest_common_substring(self, s1, s2):
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 == 0 or len_s1 == 0:
            return 0
        dp = [[0 for _ in range(len_s2+1)] for _ in range(len_s1+1)]
        max_res = 0
        for i in range(1, len_s1+1):
            for j in range(1, len_s2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1  # 前个串加1
                    max_res = max(max_res, dp[i][j])
        return max_res

    # 最长公共子序列
    def longest_common_subsequence(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        if len1 == 0 or len2 == 0:
            return
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len1][len2]

if __name__ == '__main__':
    obj = Solution()
    while True:
        s1 = input().strip()
        s2 = input().strip()

        # res = obj.longest_common_substring(s1, s2)
        res = obj.longest_common_subsequence(s1, s2)
        print(res)