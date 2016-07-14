class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = collections.Counter(t)
        window = []
        res = ""
        dic = collections.defaultdict(list)
        for i, c in filter(lambda x: x[1] in t, enumerate(s)):
            dic[c].append(i)
            window.append(i)
            
            if len(dic[c]) > counter[c]:
                window.remove(dic[c].pop(0))
            if len(window) == len(t) and (res == "" or window[-1] - window[0] < len(res)):
                res = s[window[0]:window[-1] + 1]
        return res