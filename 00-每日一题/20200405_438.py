# 滑动窗口
from collections import defaultdict
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str 模式串
        :rtype: List[int]
        """

        hash = defaultdict(int)
        p_len = len(p)
        distance = p_len  # 字符匹配距离

        for x in p:
            hash[x] += 1

        left = 0
        right = 0
        s_len = len(s)
        res = []
        while right < s_len:
            # 右指针向右移，移的过程 distance可能变小
            if hash[s[right]] > 0:  # s有p的字母
                distance -= 1

            hash[s[right]] -= 1  # 右移一次，就会匹配一个
            right += 1
            if distance == 0:  # 匹配了所有p中的字母
                res.append(left)

            if right - left == p_len:  # 窗口等于p大小，左指针可以开始移了
                if hash[s[left]] >= 0:  # 移的左指针原来是匹配的, 非负的就对了，负的前面right移的时候是没有。 因为可能s是重复的字母，所以有大于
                    distance += 1
                hash[s[left]] += 1  # 左指针在的位置，恢复
                left += 1

        return res


if __name__ == '__main__':

    obj = Solution()
    while True:
        s = input().strip()
        p = input().strip()
        res = obj.findAnagrams(s, p)
        print(res)

