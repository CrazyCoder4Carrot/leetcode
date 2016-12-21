class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def convert2set(val, nums, length):
            set_list = []
            for i in range(length):
                if val & (1 << i):
                    set_list.append(nums[i])
            return set_list

        length = len(nums)
        count = 1 << length
        for i in range(count):
            res.append(convert2set(i, nums, length))
        return res

sol  = Solution()
print sol.subsets([1,2,3])
