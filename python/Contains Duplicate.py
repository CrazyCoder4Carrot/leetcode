class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s =set()
        for num in nums:
        	if num in s:
        		return True
        	else:
        		s.add(num)
        return False

solution = Solution()
nums = [1,2,3,4,4]
#print nums
print solution.containsDuplicate(nums)