
class Solution(object):
    def multiply(self, nums1, nums2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(nums1) + len(nums2))
        for i, e1 in enumerate(reversed(nums1)):
            for j, e2 in enumerate(reversed(nums2)):
                res[i + j] += int(e1) * int(e2)
                res[i + j + 1] += res[i+j] / 10
                res[i + j] %= 10
        while len(res) > 1 and res[-1] == 0: res.pop()
        return "".join(map(str, res[::-1]))