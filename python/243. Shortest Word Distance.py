class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = len(words)
        p1 = p2 = len(words)
        for k , v in enumerate(words):
            if v == word1:
                p1 = k
                res = min(res, abs(p2-p1))
            if v == word2:
                p2 = k
                res = min(res, abs(p2-p1))
        return res