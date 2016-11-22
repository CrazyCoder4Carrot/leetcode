class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        length = len(words)
        for i in range(length):
            for j in range(len(words[i])):
                if j >= length or i >= len(words[j]) or words[i][j] != words[j][i]: 
                    return False
        return True