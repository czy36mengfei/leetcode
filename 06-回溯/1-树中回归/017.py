# 电话号码的字母组合
class Solution(object):
    phone_digits = [" ", "", "abc", "def", "ghi", "jkl", "mno",
                    "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        length = len(digits)
        if length == 0:
            return []
        res = []

        self._dfs(digits, 0, '', res)
        return res

    def _dfs(self, digits, index, pre, res):
        if index == len(digits):
            res.append(pre)
            return

        for c in self.phone_digits[int(digits[index])]:
            self._dfs(digits, index+1, pre+c, res)


if __name__ == '__main__':
    obj = Solution()
    while True:
        digits = input().strip()
        res = obj.letterCombinations(digits)
        print(res)
