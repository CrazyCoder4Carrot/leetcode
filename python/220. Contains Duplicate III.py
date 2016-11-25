class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 :
            return False
        w = t + 1
        dic = {}
        for i in range(len(nums)):
            index = nums[i] / w
            if index in dic:
                return True
            if index - 1 in dic and abs(nums[i] - dic[index - 1]) < w:
                return True
            if index + 1 in dic and abs(nums[i] - dic[index + 1]) < w:
                return True
            dic[index] = nums[i]
            if i >= k:
                del dic[nums[i-k]/w]
        return False
        