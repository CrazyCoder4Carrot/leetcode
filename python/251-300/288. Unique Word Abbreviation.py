class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {}
        for s in set(dictionary):
            abbr = self.getAbbr(s)
            if abbr not in self.dic:
                self.dic[abbr] = 1
            else:
                self.dic[abbr] += 1
        self.set = set(dictionary)
    def getAbbr(self, string):
        if len(string) < 3:
            return string
        return string[0] + str(len(string)-2) + string[-1]
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        temp = self.getAbbr(word)
        if word not in self.set:
            return temp not in self.dic
        if word in self.set:
            return self.dic[temp] <= 1
            


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")