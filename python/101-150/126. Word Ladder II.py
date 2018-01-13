

class Solution(object):

    def getnext(self, s):
        res = []
        for i in range(len(s)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != s[i]:
                    res.append(s[:i] + c + s[i + 1:])
        return res

    def helper(self, path, res, endWord):
        if path[-1] == endWord:
            res.append(path)
            return
        for word in self.getnext(path[-1]):
            if word in self.distance and self.distance[word] - 1 == self.distance[path[-1]]:
                self.helper(path + [word], res, endWord)

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        worddic = {}
        for word in wordList:
            worddic[word] = True
        if endWord not in wordList:
            return []
        level = [beginWord]
        self.distance = {}
        self.distance[beginWord] = 0
        while level:
            temp = []
            for word1 in level:
                for word2 in self.getnext(word1):
                    if word2 in worddic and word2 not in self.distance:
                        self.distance[word2] = self.distance[word1] + 1
                        temp.append(word2)
            level = temp
        res = []
        self.helper([beginWord], res, endWord)
        return res

sol = Solution()
begin = "hit"
end = "cog"
list = ["hot","dot","dog","lot","log","cog"]
print sol.findLadders(begin, end, list)
