import collections
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res= ""
        if denominator == 0:
            return res
        if numerator == 0:
            return "0"
        if denominator < 0 and numerator < 0:
            denominator *= -1
            numerator *= -1
        if denominator < 0 or numerator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
            res = "-" + res
        res_dict = collections.defaultdict(int)
        if numerator% denominator == 0:
            return res + str(numerator/denominator)
        else:
            res = res + str(numerator / denominator) + "."
            data = ""
            lenght = 0
            r = numerator % denominator
            while r:
                if res_dict[r]:
                    index = res_dict[r]
                    res = res[:index] + "(" + res[index:] + ")"
                    break
                res_dict[r] = len(res)
                r *= 10
                res += str( r/ denominator)
                r = r % denominator
        return res
            