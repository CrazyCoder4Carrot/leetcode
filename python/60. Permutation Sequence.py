from math import factorial 
class Solution(object):
    seq = 0
    res = ""
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i for i in range(1, n + 1)]
        while n -1 >= 0:
            num, k = k / factorial(n-1), k % factorial(n-1)
            if k >0:
                res.append(str(nums[num]))
                nums.remove(nums[num])
            else:
                res.append(str(nums[num-1]))
                nums.remove(nums[num-1])
            n -= 1
        return "".join(res)