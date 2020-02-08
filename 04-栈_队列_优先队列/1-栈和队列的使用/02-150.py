# 逆波兰表达式求值
# 使用栈


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operation = ['+', '-', '*', '/']

        for t in tokens:
            if t not in operation:
                stack.append(int(t))
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                if t == '+':
                    stack.append(v1+v2)
                elif t == '-':
                    stack.append(v1-v2)
                elif t == '*':
                    stack.append(v1*v2)
                elif t == '/':
                    stack.append(int(v1/v2))  # 保留整数部分，负数是先上取整
        return stack[-1]

if __name__ == '__main__':
    obj = Solution()
    while True:
        tokens = input().strip().split()
        res = obj.evalRPN(tokens)
        print(res)
