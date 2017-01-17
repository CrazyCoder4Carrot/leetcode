class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dic = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.dic
        for char in word:
            node = node.setdefault(char, {})
        node["#"] = {}
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def find(word, node):
            if not word:
                return "#" in node
            char, word = word[0], word[1:]
            if char != ".":
                return char in node and find(word, node[char])
            return any(find(word, kid) for kid in node.values() if kid != "#")
        return find(word, self.dic)
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")