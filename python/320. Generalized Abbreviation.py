class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def convert2abbr(num, count, word):
            abbr = ""
            zero, i = 0, 0
            flag = False
            while i < count:
                if not num & (1 << i):
                    if flag:
                        zero += 1
                    else:
                        flag = True
                        zero = 1
                else:
                    if flag:
                        flag = False
                        abbr = abbr + str(zero)
                    abbr = abbr + word[i]
                i += 1
            if flag:
                abbr += str(zero)
            return abbr

        res = []
        length = len(word)
        count = 1 << length
        for i in range(count):
            res.append(convert2abbr(i, length, word))
        return res
