import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        counter = collections.Counter(magazine)
        for char in ransomNote:
            if char not in magazine:
                return False
            else:
                if counter[char] == 0:
                    return False
                else:
                    counter[char] -= 1
        return True