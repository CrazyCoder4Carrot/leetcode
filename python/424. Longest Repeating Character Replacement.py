class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = j = 0 
        res = 0
        cur = ""
        while i < len(s):
        	length = 1
        	cur = s[i]
        	temp = 0
        	for j in range(i+1, len(s)):
        		if s[j] != cur:
        			temp += 1
        		if temp > k:
        			break
        		length += 1
        	i += length
        	res = max(res, length)
        return res
sol = Solution()
print sol.characterReplacement("ABBB", 2)
