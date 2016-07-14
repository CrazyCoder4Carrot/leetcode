class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > nums[l]:
                    if target >= nums[l] and target < nums[mid]:
                        r = mid
                    else:
                        l = mid
                else:
                    if target >= nums[mid] and target <= nums[r]:
                        l = mid
                    else:
                        r = mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1