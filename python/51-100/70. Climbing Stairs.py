class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0 :
            return 0
        if n == 1:
            return 1
        slow = 1
        fast = 1
        for i in range(2, n + 1):
            temp = fast
            fast = slow + fast
            slow = temp
        return fast
            