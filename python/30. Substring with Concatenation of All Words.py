import copy
import collections
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        counter = collections.Counter(words)
        res= []
        wordlen = len(words[0])
        wordslen = len(words)
        slen = len(s)
        
        for i in range(wordlen):
            temp = copy.deepcopy(counter)
            count = 0
            head = i
            for j in range(head, slen - wordlen + 1, wordlen):
                tempword = s[j:j+wordlen]
                temp[tempword] -= 1
                while temp[tempword] < 0:
                    temp[s[head:head+wordlen]] += 1
                    head += wordlen
                if wordslen * wordlen == j + wordlen - head:
                    res.append(head)
        return res