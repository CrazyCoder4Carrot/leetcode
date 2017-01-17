class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp = target - nums[i] - nums[j]
                l, r = j + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] > temp:
                        r -= 1
                    elif nums[l] + nums[r] < temp:
                        l += 1
                    else:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
        return res