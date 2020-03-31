class WordDictionary(object):
    class Node:
        def __init__(self):
            self.is_word = False
            self.dict = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordDictionary.Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.dict:
                node.dict[c] = WordDictionary.Node()
            node = node.dict[c]
        node.is_word = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        return self.match(word, node, 0)

    def match(self, word, node, index):
        if index==len(word):
            return node.is_word  # 最后一个匹配的字符必须构成词

        if word[index] == '.':
            for key in node.dict:
                if self.match(word, node.dict[key], index+1):
                    return True
            return False
        else:
            if word[index] in node.dict:
                if self.match(word, node.dict[word[index]], index+1):
                    return True
            return False
