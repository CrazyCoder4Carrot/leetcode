class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n, q = len(A), len(B[0]), len(B)
        res = [[0] * n for _ in range(m)]
        seta = set()
        setb = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    seta.add(i)
                    continue
        for i in range(len(B[0])):
            for j in range(len(B)):
                if B[j][i] != 0:
                    setb.add(i)
                    continue
        for i in seta:
            for j in setb:
                for k in range(q):
                    res[i][j] += A[i][k] * B[k][j]
        return res