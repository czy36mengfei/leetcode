class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        max_dis = 0
        pre = -1
        x = N
        i = 0
        while x:
            if x & 1 == 1:
                if pre == -1:
                    dis = 0
                else:
                    dis = i - pre
                max_dis = max(max_dis, dis)
                pre = i
            x = x >> 1
            i += 1
        return max_dis

if __name__ == '__main__':
    obj = Solution()
    N = 22
    res = obj.binaryGap(N)
    print(res)