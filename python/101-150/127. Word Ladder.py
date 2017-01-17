class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]
        while queue:
            word, length = queue.pop(0)
            for i in range(len(word)):
                for c in [chr(x) for x in range(ord("a"), ord("z") + 1)]:
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord == endWord:
                        return length + 1
                    if newWord in wordList:
                        queue += [(newWord, length + 1)]
                        wordList.remove(newWord)
        return 0