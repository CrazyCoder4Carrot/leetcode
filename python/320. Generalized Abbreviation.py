
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count):
            if pos == len(word):
                res.append(cur + str(count) if count > 0 else cur)
            else:
                helper(word, pos + 1, cur,count + 1)
                helper(word, pos + 1, cur + (str(count) if count > 0 else "") + word[pos], 0)
        res = []
        helper(word, 0, "", 0)
        return res
