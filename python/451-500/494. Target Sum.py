import collections
class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = collections.defaultdict(int)
        if nums[0] == 0:
            dic[0] = 2
        else:
            dic[-nums[0]] = 1
            dic[nums[0]] = 1
        for i in range(1, len(nums)):
            temp = collections.defaultdict(int)
            for d in dic:
                temp[d + nums[i]] = temp[d + nums[i]] + dic[d]
                temp[d - nums[i]] = temp[d - nums[i]] + dic[d]
            dic = temp
        return dic[S]