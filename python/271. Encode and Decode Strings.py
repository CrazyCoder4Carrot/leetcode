class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return "".join("%d:".format(len(s)) + s for s in strs)
    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        if not s[0].isdigit():
            return s
        res = []
        i = 0
        while i < len(s):
            count = ""
            #print s
            while s[i] != ":":
                count = count + s[i]
                i += 1
            count = int(count)
            temp = s[i + 1:i + 1 + count]
            res.append(temp)
            i += 1 + count
        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))