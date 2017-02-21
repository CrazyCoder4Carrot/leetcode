class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dic = {}
        res = [0] * len(nums)
        for i in range(len(nums)):
            dic[nums[i]] = i
        nums.sort(reverse=True)
        for i in range(len(nums)):
            rank = str(i + 1)
            if i == 0:
                rank = "Gold Medal"
            if i == 1:
                rank = "Silver Medal"
            if i == 2:
                rank = "Bronze Medal"
            res[dic[nums[i]]] = rank
        return res
