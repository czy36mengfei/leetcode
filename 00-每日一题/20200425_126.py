class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        len_word = len(beginWord)
        forward = {beginWord}  # 改成set可以加快
        backward = {endWord}
        word_dict = set(wordList)

        alpha = list('abcdefghijklnmopqrstuvwxyz')
        res = 1
        while forward:
            tmp_set = set()
            if len(forward) > len(backward):
                forward, backward = backward, forward
            for word in forward:
                for i in range(len_word):
                    for c in alpha:
                        cur = word[:i]+c+word[i+1:]
                        if cur in backward:
                            return res + 1
                        if cur in word_dict:

                            tmp_set.add(cur)
                            word_dict.remove(cur)
            res += 1
            forward = tmp_set
        return 0



    def _ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if beginWord == endWord:
            return 1

        queue = [(1, beginWord)]
        visited = {word: False for word in wordList}
        visited[beginWord] = True
        while queue:
            level, node = queue.pop(0)
            level += 1
            for word in wordList:
                if visited[word] is False:
                    if self.able_tran(node, word):
                        if word == endWord:
                            return level
                        queue.append((level, word))
                        visited[word] = True
        return 0

    def able_tran(self, s1, s2):
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                if diff == 2:
                    return False
        return True


if __name__ == '__main__':
    obj = Solution()
    while True:
        begin_word = input().strip()
        end_word = input().strip()
        word_list = input().strip().split()
        res = obj.ladderLength(begin_word, end_word, word_list)
        print(res)
