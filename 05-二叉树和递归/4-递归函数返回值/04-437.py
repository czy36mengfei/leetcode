# 路径总和
import collections
class Solution(object):
    res = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.res = 0
        memory = collections.defaultdict(int)
        memory[0] = 1
        if root is None:
            return self.res
        self._dfs(root, memory, 0, sum)
        return self.res


    def _dfs(self, root,memory, cur_sum, target):
        if root is None:
            return
        cur_sum += root.val
        self.res += memory[cur_sum-target] # 到某个节点的差距是target

        # 可以以当前遍历节点为起点
        memory[cur_sum] += 1  # 可能有多个路径共用一个节点
        if root.left:
            self._dfs(root.left, memory, cur_sum, target)
        if root.right:
            self._dfs(root.right, memory, cur_sum, target)
        memory[cur_sum] -= 1  # 当前节点不在为起点
