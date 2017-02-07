class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        index_dic = {}
        for i in range(len(nums)):
            index_dic[nums[i]] = i
        res = [-1] * len(findNums)
        for i in range(len(findNums)):
            for j in xrange(index_dic[findNums[i]] + 1, len(nums)):
                if nums[j] > findNums[i]:
                    res[i] = nums[j]
                    break
        return res