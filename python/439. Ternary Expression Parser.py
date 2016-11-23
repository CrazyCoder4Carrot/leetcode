class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def parseOne(s):
            return s[2] if s[0] == "T" else s[4]
        stack = []
        for c in expression:
            stack.append(c)
        expr = ""
        while stack:
            while stack[-1] != "?":
                expr = stack.pop() + expr
            expr = stack.pop() + expr
            expr = stack.pop() + expr
            expr = parseOne(expr[:5]) + expr[5:]
        return expr
sol = Solution()
print sol.parseTernary("T?T?F:5:3")
