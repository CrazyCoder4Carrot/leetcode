class Solution(object):

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []

        def dfs(num, path, cur, last, target):
            if not num:
                print path, cur, last
            if not num:
                if cur == target:
                    res.append(path)
                return
            for i in range(1, len(num) + 1):
                val = num[:i]
                if i == 1 or (i > 1 and num[0] != "0"):
                    dfs(num[i:], path + "+" + val,
                        cur + int(val), int(val), target)
                    dfs(num[i:], path + "-" + val, cur -
                        int(val), -int(val), target)
                    dfs(num[i:], path + "*" + val, cur - last +
                        last * int(val),  last * int(val), target)
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), target)
        return res


sol = Solution()
print sol.addOperators("123", 6)