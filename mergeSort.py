class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        res = self.mergeSort(A)
    def mergeSort(self, A):
        length = len(A)
        if length <= 1:
            return A
        l1 = self.mergeSort(A[:length /2])
        l2 = self.mergeSort(A[length/2:])
        #print l1, l2
        self.merge(l1, l2, A)
        #print l3
        return A
    def merge(self, l1, l2, A):
        #print l1,l2
        k = i = j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                A[k] = l1[i]
                i += 1
                k += 1
            else:
                A[k] = l2[j]
                j += 1
                k += 1
        while i < len(l1):
            A[k] = l1[i]
            i += 1
            k += 1
        while j < len(l2):
            A[k] = l2[j]
            j += 1
            k += 1
        return A