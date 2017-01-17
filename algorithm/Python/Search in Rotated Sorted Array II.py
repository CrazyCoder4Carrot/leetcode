class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums = list(set(nums))
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return True
            else:
                if nums[mid] > nums[lo]:
                    if target >= nums[lo] and target <= nums[mid]:
                        hi = mid -1 
                    else:
                        lo = mid + 1
                else:
                    if target <= nums[hi] and target >= nums[mid]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                
        return False