class NumArray(object):
    def __init__(self, nums):
        
        #initialize your data structure here.
        #type nums: List[int]
        self.nums = nums
        #print self.nums

    def sumRange(self, i, j):
        sum = 0
        while i <= j:
            sum += self.nums[i]
            i += 1
        print sum


nums = [-2,0,3,-5,2,-1]
numArray = NumArray(nums)
numArray.sumRange(0,2)
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)