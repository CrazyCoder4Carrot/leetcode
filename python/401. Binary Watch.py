import collections
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        dicthour = collections.defaultdict(list)
        dictminute = collections.defaultdict(list)
        for i in range(12):
            dicthour[bin(i).count("1")].append(str(i))
        for i in range(60):
            dictminute[bin(i).count("1")].append("{:02d}".format(i))
        res = []
        for i in range(num + 1):
            res += [hour+":"+minute for hour in dicthour[i] for minute in dictminute[num-i]]
        return res