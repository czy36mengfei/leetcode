# 有效的括号
# 使用栈


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_list = ['()', '[]', '{}']
        stack = []
        for c in s:
            stack.append(c)
            # 匹配时出栈
            if len(stack) >= 2 and stack[-2] + stack[-1] in valid_list:
                stack.pop()
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = Solution()
    while True:
        s = input().strip()
        res = obj.isValid(s)
        print(res)
