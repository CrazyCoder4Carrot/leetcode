import collections
import sys
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dict = collections.defaultdict(list)
        for i in range(len(words)):
            self.dict[words[i]].append(i)
        self.res = {}

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def diff(word1, word2):
            minval = sys.maxint
            for i in self.dict[word1]:
                for j in self.dict[word2]:
                    minval = min(minval, abs(i-j))
            return minval
        if (word1, word2) in self.res:
            return self.res[(word1, word2)]
        if (word2, word1) in self.res:
            return self.res[(word2, word1)]
        minval = diff(word1, word2)
        self.res[(word1, word2)] = minval
        return minval


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")