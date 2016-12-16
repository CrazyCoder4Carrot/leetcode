import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dict1 = collections.defaultdict(int)
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                dict1[A[i] + B[j]] += 1
        for i in range(len(C)):
            for j in range(len(D)):
                res += dict1[-(C[i] + D[j])]
        return res