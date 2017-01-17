import collections
class Solution(object):
    def wordSquares(self, words):
        n = len(words[0])
        fulls = collections.defaultdict(list)
        for word in words:
            for i in range(n):
                fulls[word[:i]].append(word)
        def build(suqare):
            if len(square) == n:
                squares.append(square)
                return
            for word in fulls["".join(zip(*square)[len(square)])]:
                build(square+[word])
        square = []
        for word in words:
            build([words])
        return squares

sol = Solution()
print sol.wordSquares(["abat","baba","atan","atal"])