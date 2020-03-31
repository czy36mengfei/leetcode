class Trie(object):
    class Node:
        def __init__(self):
            self.is_word = False  # 是一个单词结尾的标志
            self.dict = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.dict:
                node.dict[c] = Trie.Node()
            node = node.dict[c]
        node.is_word = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.dict:
                return False
            else:
                node = node.dict[c]
        return node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.dict:
                return False
            else:
                node = node.dict[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)