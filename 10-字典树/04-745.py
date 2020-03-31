class WordFilter(object):
    class Node:
        def __init__(self):
            self.val = -1
            self.dict = dict()

    def _findall(self, node, res):

        for key in node.dict:
            self._findall(node.dict[key], res)
        # 要遍历出所有，所以最后才访问自己
        if node.val != -1:
            res.append(node.val)
            return

    def _start_with(self, predix):
        node = self.root
        res = []
        if predix in self.pre_visited:
            return self.pre_visited[predix]
        for c in predix:
            if c in node.dict:
                node = node.dict[c]
            else:
                return []
        self._findall(node, res)
        res = sorted(res)
        self.pre_visited[predix] = res
        return res

    def _insert(self, word, value):
        node = self.root
        for c in word:
            if c not in node.dict:
                node.dict[c] = WordFilter.Node()
            node = node.dict[c]
        node.val = value

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = WordFilter.Node()
        self.words = words
        self.pre_suf_visited = dict()
        self.pre_visited = dict()
        for i, word in enumerate(words):
            self._insert(word, i)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """

        if prefix == '':
            pre_res = [i for i in range(len(self.words))]
        else:
            pre_res = self._start_with(prefix)

        for i in range(len(pre_res) - 1, -1, -1):
            index = pre_res[i]
            # 利用保存的答案
            if suffix in self.pre_suf_visited and \
                    self.words[index] in self.pre_suf_visited[suffix]:
                return index
            if self.words[index].endswith(suffix):
                if suffix not in self.pre_suf_visited:
                    self.pre_suf_visited[suffix] = set()
                self.pre_suf_visited[suffix].add(self.words[index])
                return index
        return -1


if __name__ == '__main__':
    words = ['apple']
    prefix, suffix = 'a', 'e'

    obj = WordFilter(words)
    param_1 = obj.f(prefix, suffix)
    print(param_1)
