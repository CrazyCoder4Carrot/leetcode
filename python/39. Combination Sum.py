class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = sorted(candidates)
        self.helper(candidates, target, res, [])
        return res
    def helper(self, candidates, target, res, temp):
        if target == 0:
            res.append(temp)
            return
        for item in candidates:
            if item > target:
                break
            if temp and item < temp[-1]:
                continue
            else:
                self.helper(candidates, target - item, res, temp + [item])