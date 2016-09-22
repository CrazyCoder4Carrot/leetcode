class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, combines = [(n, 2, [])], []
        while res:
        	n, i, combine = res.pop()
        	while i * i  <= n:
        		if n % i == 0:
        			combines += [combine + [i, n/i]]
        			res += [(n/i, i, combine + [i])]
        		i += 1
        return combines