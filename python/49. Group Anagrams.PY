from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for val in strs:
            dic["".join(sorted(val))] += [val]
        return [value for key, value in dic.items()]