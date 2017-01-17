class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        start, end = nums[0], nums[0]
        if len(nums) == 1:
            return [str(nums[0])]
        new = False
        res = []
        i = 1
        while i < len(nums):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end: 
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start = end = nums[i]
            if i + 1 >= len(nums):
                if start == end: 
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
            i += 1
        return res
                