# 简化路径
# 使用栈

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []
        path_list = path.split('/')
        for p in path_list:
            if p in ['', '.']:
                continue
            elif p == '..':
                if len(stack) >= 1:
                    stack.pop()
            else:
                stack.append(p)

        res = '/' + '/'.join(stack)
        return res
if __name__ == '__main__':
    obj = Solution()
    while True:
        path = input().strip()
        res = obj.simplifyPath(path)
        print(res)
