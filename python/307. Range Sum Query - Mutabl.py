class BinaryIndexTree(object):
    def __init__(self, n):
        self.arr = [0] * (n+1)
        self.n = n
        
    def lowbit(self, x):
        return x & (-x)
        
    def update(self, x, val):
        x = x + 1
        while x <= self.n:
            self.arr[x] += val
            x += self.lowbit(x)
            
    def sum(self, x):
        x += 1
        res = 0
        while x > 0:
            res += self.arr[x]
            x -= self.lowbit(x)
        return res
        
    def construct(self, nums):
        for i in range(len(nums)):
            self.update(i, nums[i])

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.bit = BinaryIndexTree(len(nums))
        self.bit.construct(nums)
        self.nums = nums
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.bit.update(i, diff)
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.bit.sum(j) - self.bit.sum(i) + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)