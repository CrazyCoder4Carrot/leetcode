class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1 + l2:
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        dp = [[False] * (l1 + 1) for _ in range(l2 + 1) ]
        dp[0][0] = True
        for j in range(1, l1 + 1):
            if s1[:j] == s3[:j]:
                dp[0][j] = True
        for i in range(1, l2 + 1):
            if s2[:i] == s3[:i]:
                dp[i][0] = True
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                dp[i][j] = (dp[i-1][j] and s2[i-1] ==s3[i+j-1] ) or (dp[i][j-1] and s1[j-1] == s3[i+j-1])
        return dp[-1][-1]
        
                
            
        