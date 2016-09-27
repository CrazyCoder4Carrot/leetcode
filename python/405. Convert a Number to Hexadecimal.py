class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        hexnum = "0123456789abcdef"
        bin = self.tobinary(num)
        res = ""
        for i in range(0, len(bin)/4):
            res += self.seghex(bin[i*4:i*4 + 4], hexnum)
        return res
    def tobinary(self, num):
        res = ""
        base = "0" * 32
        if num > 0:
            while num:
                if num % 2 == 0:
                    res = "0" + res
                else:
                    res = "1" + res
                num = num /2
            while len(res) % 4 != 0:
                res = "0" + res
        else:
            num = abs(num)
            while num:
                if num % 2 == 0:
                    res = "0" + res
                else:
                    res = "1" + res
                num = num /2
            res = "0" * (32 - len(res)) + res
            res = (["1" if i == "0" else "0" for i in res])
            carry = 1
            for i in range(len(res)-1, -1, -1):
                if res[i] == "1" and carry == 0:
                    res[i] = "1"
                    carry = 0
                    continue
                if res[i] == "0" and carry == 1:
                    res[i] = "1"
                    carry = 0 
                    continue
                if res[i] == "0" and carry == 0:
                    res[i] = "0"
                    carry = 0
                    continue
                if res[i] == "1" and carry == 1:
                    res[i] = "0"
                    carry = 1
                    continue
        return "".join(res)
    def seghex(self, string, hexnum):
        sum = 0
        for i in range(len(string)):
            sum += int(string[i]) * 2 ** (len(string) - 1 - i)
        return hexnum[sum]