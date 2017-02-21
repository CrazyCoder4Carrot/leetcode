class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        def oneRow(string):
            r1 = r2 = r3 = 0
            string = string.lower()
            for c in string:
                if c in row1:
                    r1 = 1
                if c in row2:
                    r2 = 1
                if c in row3:
                    r3 = 1
            count = r1 + r2 + r3
            return count == 1
        return filter(lambda x: oneRow(x), words)