class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                if abbr[j].isdigit():
                    res = ""
                    while j < len(abbr) and abbr[j].isdigit():
                        res = res + abbr[j]
                        j += 1
                    res = int(res)
                    print res
                    i = i + res
                else:
                    return False
        print i , len(word), j, len(abbr)
        return i == len(word)
sol = Solution()
s = "internationalization"
abbr = "i12iz4n"
print sol.validWordAbbreviation(s, abbr)