class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        keys = []
        for i in xrange(1, n + 1):
            key = i
            while key < 10000000:
                key *= 10
            keys.append(key * 10000000 + i)
        keys.sort()
        return [key % 10000000 for key in keys]
        
                
        
        


