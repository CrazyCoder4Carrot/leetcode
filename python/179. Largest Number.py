class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        res = "".join(sorted(map(str, nums), cmp = lambda x, y: cmp(y + x, x + y)))
        return res if res[0] != "0" else "0"