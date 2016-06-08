
class segmentTree:
    def __init__(self, low, high, left = None, right=None):
        self.low = low
        self.high = high
        self.left = left
        self.right = right
        self.sumval = 0
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.arr = nums
        self.root = self.buildTree(nums, 0, len(nums) - 1)
    def buildTree(self, nums, low, high):
        if not nums:
            return None
        if low > high:
            return None
        mid = (low + high) / 2
        root = segmentTree(low, high)
        if low == high:
            root.sumval = nums[low]
            return root
        root.left = self.buildTree(nums, low, mid)
        root.right = self.buildTree(nums, mid + 1, high)
        root.sumval = root.left.sumval + root.right.sumval
        return root
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.updateTree(self.root, i, val)
    def updateTree(self, root, i ,val):
        if i < 0 or i > len(self.arr):
            return 
        if not root:
            return
        mid = (root.low + root.high) / 2
        if root.low == root.high and root.low == i:
            root.sumval = val
            return
        if i <= mid:
            self.updateTree(root.left, i, val)
        else:
            self.updateTree(root.right, i ,val)
        root.sumval = root.left.sumval + root.right.sumval

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(self.root, i, j)
    def query(self, root, i, j):
        if not root or i > j:
            return 0
        if root.low == i and root.high == j:
            return root.sumval
        mid = (root.low + root.high) / 2
        if root.low <= i and mid >= j:
            return self.query(root.left, i, j)
        if i > mid:
            return self.query(root.right, i, j)
        return self.query(root.left, i, mid) + self.query(root.right, mid + 1, j)