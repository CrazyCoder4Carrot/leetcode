class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        d = self.root.dic
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
            print self.root.dic
        d["#"] = "#"
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        d = self.root.dic.copy()
        for c in word:
            if c in d:
                d = d[c]
            else:
                return False
        if "#" in d:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        d = self.root.dic.copy()
        for c in prefix:
            if c in d:
                d = d[c]
            else:
                return False
        return True
trie = Trie()
trie.insert("somestring")
trie.insert("tomestring")
print trie.root.dic
trie.search("key")