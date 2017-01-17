class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        odd = ["0","1","8"]
        even = ["00","11", "69", "88", "96"]
        if n == 1:
            return odd
        if n == 2:
            return even[1:]
        if n % 2 == 0:
            formers = self.findStrobogrammatic(n-2)
            res = []
            for former in formers:
                for val in even:
                    #if former[0][0] != "0":
                    res.append(former[:len(former)/2] + val + former[len(former)/2:])
            return sorted(res)
        else:
            formers = self.findStrobogrammatic(n-1)
            res = []
            for former in formers:
                for val in odd:
                    #if former[0][0] !=  "0":
                    res.append(former[:(len(former)+1)/2] + val + former[(len(former)+1)/2:])
            return sorted(res)
                    
            