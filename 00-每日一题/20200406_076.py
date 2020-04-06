# 滑动窗口
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_len = len(t)
        s_len = len(s)
        t_dict = {}
        for c in t:
            if c not in t_dict:
                t_dict[c] = 0
            t_dict[c] += 1

        res_str = s
        if t_len == 0 or s_len == 0:
            return ""
        res = []
        left = 0
        right = 0
        distance = t_len

        while right < s_len:
            if s[right]in t_dict:
                if t_dict[s[right]] > 0:
                    distance -= 1  # 第一次，移除这个字符
                t_dict[s[right]] -= 1

            right += 1

            if distance == 0:  # 找到了答案， left才有左移的必要
                # res.append(s[left:right])

                # 里面至少要留一个t中的字符
                while True:

                    if s[left] in t_dict and t_dict[s[left]] < 0:
                        t_dict[s[left]] += 1  # 匹配的字符少了一个
                        left += 1  # 有多的left 右移
                        continue
                    if s[left] not in t_dict:
                        left += 1  # 没有的left 右移
                        continue

                    break

                single_s = s[left:right]
                if len(single_s) < len(res_str):
                    res_str = single_s
        if distance != 0:
            return ""

        return res_str

if __name__ == '__main__':
    obj = Solution()
    while True:
        s = input().strip()
        t = input().strip()
        res = obj.minWindow(s, t)
        print(res)





