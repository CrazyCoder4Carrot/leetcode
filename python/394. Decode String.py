class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = ""
        nums = "0123456789"
        alpha = "abcdefghijklmnopqrstuvwxyz"
        temp = ""
        i = 0
        while i < len(s):
            if s[i] == "[":
                stack.append(s[i])
                i += 1
            if s[i] == "]":
                print stack
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                count = stack.pop()
                res = int(count) * temp
                stack.append(res)
                i += 1
            if i < len(s) and s[i] in nums:
                j = i
                while j < len(s) and s[j] in nums:
                    j += 1
                num = s[i:j]
                i = j
                stack.append(num)
            if  i < len(s) and s[i] in alpha:
                j = i
                while j < len(s) and s[j] in alpha:
                    j += 1
                substring = s[i:j]
                i = j
                stack.append(substring)
        return "".join(stack)
    
                