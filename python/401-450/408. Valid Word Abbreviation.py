class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        temp = 0
        digit = ""
        count, i = 0, 0
        flag = False
        while i < len(abbr):
            if abbr[i].isalpha():
                if flag:
                    temp = temp << int(digit)
                    flag = False
                    digit = ""
                temp = (temp << 1) | 1
                i += 1
            while i < len(abbr) and (abbr[i].isdigit()):
                flag = True
                digit += abbr[i]
                i += 1
        if flag:
            temp = temp << int(digit)
        print bin(temp)

        if temp > (1 << len(word)):
            return False
        count, i = 0, 0
        res = ""
        flag = False
        length = len(word)
        while i < length:
            if temp & (1 << i):
                if flag:
                    res = str(count) + res
                    count = 0
                    flag = False
                res = word[length - i - 1] + res
                i += 1
            while i < length and ((temp & 1 << i) == 0):
                flag = True
                count += 1
                i += 1
        if flag:
            res = str(count) + res
        print res
        return res == abbr
