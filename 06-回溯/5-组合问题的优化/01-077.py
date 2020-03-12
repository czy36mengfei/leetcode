# 使用剪枝优化
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 or k < 1 or n < k:
            return []
        res = []
        self._dfs(1, n, k, [], res)
        return res

    def _dfs(self, start, n, k, pre, res):
        if len(pre) == k:
            # 必须使用pre[:]或pre，这样才会新建一个对象，不然只是copy引用
            res.append(pre[:])
            return

        for i in range(start, (n+1)-(k-len(pre))+1):
            # max(i) + 接下来要选择的元素个数 - 1 = n
            pre.append(i)
            self._dfs(i+1, n, k, pre, res)
            pre.pop()

if __name__ == '__main__':
    obj = Solution()
    while True:
        nums = input().strip().split()
        n, k = int(nums[0]), int(nums[1])
        res = obj.combine(n, k)
        print(res)

