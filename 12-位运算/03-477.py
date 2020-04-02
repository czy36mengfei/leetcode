# 汉明距离的总和，等于每一个二进制位上的汉明距离的总和。所以两两之间的汉明距离的总和，转换为针对每个bit位置的两两之间汉明距离的总和。对于固定位置的bit，如每1个bit，两两之间的汉明距离的总和实际上为：1的个数*0的个数。
# 统计每个二进制位 1 的个数和 0 的个数, 按照每个二进制位的不同将数组分为两组；一组是第 i 位为 1，一组是第 i 位为 0; 数据的两两组合表示为这两组数据之间的全排列 即其个数相乘

# 汉明距离总和等于每位上的汉明距离总和
# 每位的汉明总和就是一个选1，一个选0有多少种：即1的个数乘0的个数

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_0, cnt_1 = 0, 0
        res = 0
        for i in range(32):
            cnt_0, cnt_1 = 0, 0
            for n in nums:
                if (n >> i) & 1:  # 移到倒数第i位，看是不是1
                    cnt_1 += 1
                else:
                    cnt_0 += 1
            res += cnt_0 * cnt_1
        return res
