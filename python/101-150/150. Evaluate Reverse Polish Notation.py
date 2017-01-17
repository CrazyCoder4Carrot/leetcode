class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c not in "+-*/":
                val = int(c)
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if c == "+":
                    val = val1 + val2
                if c == "-":
                    val = val1 - val2
                if c == "*":
                    val = val1 * val2
                if c == "/":
                    if val1 * val2 < 0 and val1 % val2 != 0:
                        val = val1 / val2 + 1
                    else:
                        val = val1 / val2
            stack.append(val)
        return stack[-1]
            