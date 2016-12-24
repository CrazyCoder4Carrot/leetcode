class Solution(object):

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = [("", 0)] * 256
        for c in s:
            index = ord(c)
            char, count = a[index]
            char = c
            count += 1
            a[index] = (char, count)
        a.sort(key=lambda x: x[1], reverse=True)
        res = ""
        for char, count in a:
            res += char * count
        return res
