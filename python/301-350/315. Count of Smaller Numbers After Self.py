class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def cal(nums, low, high, res):
            if low > high:
                return 0,0
            if low == high:
                return low, high
            if low < high:
                mid = (low + high) / 2
                low1, high1 = cal(nums, low, mid, res)
                low2, high2 = cal(nums, mid+1, high, res)
                for i in range(low1, high1 + 1):
                    for j in range(low2, high2 + 1):
                        if nums[i] > nums[j]:
                            res[i] += 1
                return low, high
        res = [0] * len(nums)
        cal(nums, 0, len(res) - 1, res)
        return res
