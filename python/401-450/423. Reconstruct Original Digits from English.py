import collections
class Solution(object):

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        dict = collections.Counter(s)
        print dict
        if "w" in dict:
            res += [2] * dict["w"]
            dict["t"] -= dict["w"]
            dict["o"] -= dict["w"]
            print res
        if "z" in dict:
            res += [0] * dict["z"]
            dict["o"] -= dict["z"]
        if "u" in dict:
            res += [4] * dict["u"]
            dict["f"] -= dict["u"]
            dict["o"] -= dict["u"]
        if "x" in dict:
            res += [6] * dict["x"]
            dict["s"] -= dict["x"]
        if "g" in dict:
            res += [8] * dict["g"]
            dict["h"] -= dict["g"]
        if "s" in dict:
            res += [7] * dict["s"]
            dict["v"] -= dict["s"]
            dict["n"] -= dict["s"]
        if "h" in dict:
            res += [3] * dict["h"]
        if "f" in dict:
            res += [5] * dict["f"]
        if "o" in dict:
            res += [1] * dict["o"]
            dict["n"] -= dict["o"]
        if "n" in dict:
            res += [9] * (dict["n"] / 2)
        return "".join(map(str, sorted(res)))


sol = Solution()
print sol.originalDigits("owoztneoer")
