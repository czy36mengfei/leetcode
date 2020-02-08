# 动态规划，整数分割
class Solution(object):
    def numDecodings(self, s):
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            return 1 if s[0] != '0' else 0
        mem = [0] * length
        mem[0] = 1 if s[0] != '0' else 0
        for i in range(1, length):
            if s[i] != '0':
                mem[i] += mem[i-1]
            if 9 < int(s[i-1:i+1]) < 27:  # 特例 01
                if i - 2 < 0:
                    mem[i] += 1
                else:
                    mem[i] += mem[i-2]
        return mem[length-1]
if __name__ == '__main__':
    obj = Solution()
    while True:
        s = input().strip()
        res = obj.numDecodings(s)
        print(res)
