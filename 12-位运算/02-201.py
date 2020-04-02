# 只要从m到n的过程中，产生过进位，那么包括进位，及其右边的位，最终与的结果一定是0。因此，比较的其实是m和n从左侧起，最长的相同部分
# 首位从不同的位开始， 后面的位肯定有0 0xx->100


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while n != m:
            n = n >> 1
            m = m >> 1
            i += 1
        return n << i

    def _rangeBitwiseAnd(self, m, n):
        # 把后面的一全变0
        # n和m的差别 就是 总有一位n为1，m为0， 前面都一样
        while n > m:
            n = n & (n-1)  # 把右边第一个1变为0
        return n

if __name__ == '__main__':
    obj = Solution()
    obj.rangeBitwiseAnd(5,7)