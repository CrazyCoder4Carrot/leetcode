class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(A) - 2):
            j = i + 1
            gap = A[j] - A[i]
            while j < len(A) and A[j] - A[j-1] == gap:
                j += 1
            if j - i + 1 >= 3:
                res += j - i - 3 + 1
        return res
                    