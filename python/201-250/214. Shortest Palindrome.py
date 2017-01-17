class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        A = s + "*" + s[::-1]
        count = [0]
        for i in range(1, len(A)):
        	index = count[i-1]
        	while index > 0 and A[index] != A[i]:
        		index = count[index-1]
        	count.append(index + (1 *(A[index] == A[i])))
        return s[count[-1]:][::-1] + s