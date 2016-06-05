# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(version):
	if version == 3:
		return True
	else:
		return False
upper = 0 
low = 0
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = n
        l = 1
        while(l <= r):
        	mid = l + (r - 1)/2
        	if isBadVersion(mid) == False:
        		l = mid + 1
        	else:
        		r = mid - 1
        return l
