class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        
        for s in strings:
            shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
            d[shift].append(s)
        
        return d.values()