class Solution(object):
    class Node:
        def __init__(self):
            self.index = -1
            self.dict = dict()

    def __init__(self):
        self.root = Solution.Node()

    def _insert(self, word, index):
        node = self.root
        for c in word:
            if c not in node.dict:
                node.dict[c] = Solution.Node()
            node = node.dict[c]
        node.index = index

    def _dfs(self, node, res):
        if not node.dict:
            # if node.index != -1:  能进来就不会等于-1
            res.append(node.index)
            return
        has_son = False
        for key in node.dict:
            son_node = node.dict[key]
            if son_node.index == -1:
                continue
            has_son = True
            self._dfs(son_node, res)
        if has_son is False:
            # 孩子中没有是词的
            res.append(node.index)
        return

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 0:
            return ''

        for i, word in enumerate(words):
            self._insert(word, i)

        res = []
        self._dfs(self.root, res)
        res = sorted(res)
        if not res:
            return ''
        else:

            res_str = words[res[0]]
            max_len = len(res_str)
            for i in range(1, len(res)):
                now_word = words[res[i]]
                if len(now_word) > max_len or \
                        len(now_word) == max_len and now_word < res_str:
                    res_str = words[res[i]]
                    max_len = len(now_word)
        return res_str


if __name__ == '__main__':
    obj = Solution()
    words = ["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]
    res = obj.longestWord(words)
    print(res)
