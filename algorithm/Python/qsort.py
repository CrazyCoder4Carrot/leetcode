class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        self.qsort(A, 0, len(A) - 1)
    def qsort(self, A, start, end):
        if start < end: 
            r = self.partition(A, start, end)
            self.qsort(A, start, r - 1)
            self.qsort(A, r+1, end)
    def partition(self, A, start, end):
        x = A[end]
        i = start - 1
        for j in range(start, end):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[end] = A[end], A[i+1]
        return i + 1

sln = Solution()
A = [3,2,8,45,2,6,9]
sln.sortIntegers2(A)
print A