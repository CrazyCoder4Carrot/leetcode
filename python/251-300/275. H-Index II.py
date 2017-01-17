class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        l, r = 0, len(citations) - 1
        n = len(citations)
        while l <= r:
            mid = (l + r) / 2
            if citations[mid] == n - mid:
                return n - mid
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        return n - l
                