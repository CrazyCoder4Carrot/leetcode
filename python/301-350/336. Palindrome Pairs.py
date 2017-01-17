class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wmap = {y : x for x, y in enumerate(words)}
        ans = set()
        for idx, word in enumerate(words):
        	#the word itself is pal
        	if "" in wmap and word != "" and word == word[::-1] :
        		bidx = wmap[""]
        		ans.add([bidx, idx])
        		ans.add([idx, bidx])
        	rword = word[::-1]
        	#the word's pal in the dictionary
        	if rword in wmap:
        		ridx = wmap[rword]
        		if idx != ridx:
        			ans.add([idx, ridx])
        			ans.add([ridx, idx])
        	#divide the word into two parts.
        	for x in range(1, len(word)):
        		left, right = word[:x], word[x:]
        		rleft, rright = left[::-1], right[::-1]
        		if left == left[::-1] and rright in wmap:
        			ans.add([wmap[rright]], idx)
        		if right == right[::-1] and rleft in wmap:
        			ans.add([idx, wmap[rleft]])
        return list(ans)