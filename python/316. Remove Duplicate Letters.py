import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        stack = []
        res_set = set()
        for c in s:
            counter[c] -= 1
            if c in res_set:
                continue
            while stack and stack[-1] > c and counter[stack[-1]]:
                print stack
                temp = stack.pop()
                res_set.remove(temp)
            stack.append(c)
            res_set.add(c)
        return "".join(stack)
                
                