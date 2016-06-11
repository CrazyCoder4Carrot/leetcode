class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if not nums1 or not nums2:
            return res
        mapdict = {}
        for val in nums1:
            if val in mapdict:
                mapdict[val] += 1
            else:
                mapdict[val] = 1
        for val in nums2:
            if val in mapdict and mapdict[val] > 0:
                mapdict[val] -=1
                res.append(val)
        return res