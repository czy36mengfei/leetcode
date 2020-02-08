# 找数组中两个数最大的异或值
class Solution(object):
    class TreeNode:
        def __init__(self):
            # 0为左，1为右
            self.left = None
            self.right = None
            self.index = -1
    def __init__(self):
        self.root = Solution.TreeNode()

    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 2:
            return nums[0] ^ nums[1]
        # 构建字典树
        for t, num in enumerate(nums):
            node = self.root
            for i in range(31, -1, -1):
                # if i == 4:
                #     print('debug')
                if num >> i & 1 == 0:   # 从高到底，各位是否为1
                    if not node.left:  # 不存在才要建新的的
                        node.left = Solution.TreeNode()
                    node = node.left
                else:
                    if not node.right:
                        node.right = Solution.TreeNode()
                    node = node.right
            node.index = t

        # 从高位起，先找反的，不行再找同的
        res = 0
        max_i = -1  # 找到出现不同最高的那一位，比它小就不要

        for num in nums:
            node = self.root
            find_max_i = True
            for i in range(31, -1, -1):
                # if i == 4:
                #     print('debug')
                if find_max_i is True and i < max_i:  # 异或值肯定比原来小，不用找了
                    break
                if num >> i & 1 == 0:
                    if node.right:  # 取反向
                        if find_max_i is True and i >= max_i:
                            max_i = i
                            find_max_i = False
                        node = node.right
                    elif node.left:
                        node = node.left
                else:
                    if node.left:
                        if find_max_i is True and i >= max_i:
                            max_i = i
                            find_max_i = False
                        node = node.left
                    elif node.right:
                        node = node.right


            if find_max_i is True:
                # 没有找到最大的就退出了
                continue

            # 找到的当前最高位
            t = node.index
            other = nums[t]
            res = max(res, num ^ other)
        return res

    def _findMaximumXOR(self, nums):

        # 找前缀
        mask = 0
        res = 0
        for i in range(31, -1, -1):
            mask |= 1 << i

            # 得到前缀
            pre = set()
            for num in nums:
                pre.add(num & mask)

            tmp = res | 1 << i  # 尝试该位为1，正确才赋值
            for p in pre:
                if tmp ^ p in pre:
                    res = tmp
                    break
        return res




if __name__ == '__main__':
    obj = Solution()
    nums = [3, 10, 5, 25, 2, 8]
    res = obj._findMaximumXOR(nums)
    print(res)



