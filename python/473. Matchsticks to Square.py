class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        sumval = sum(nums)
        if sumval % 4 != 0:
            return False
        target = [sumval/4] * 4
        nums.sort(reverse = True)
        def dfs(nums, index, target):
            if index == len(nums):
                return True
            for i in range(4):
                if target[i] >= nums[index]:
                    target[i] -= nums[index]
                    if dfs(nums, index + 1, target):
                        return True
                    target[i] += nums[index]
            return False
        return dfs(nums, 0, target)