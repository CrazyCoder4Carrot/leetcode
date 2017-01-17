import itertools
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        return sorted(itertools.product(nums1, nums2), key=sum)[:k]