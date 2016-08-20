class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []
    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        low = timestamp - 300
        hi = timestamp
        i = 0
        count = 0 
        while i < len(self.hits):
            if self.hits[i] <= low:
                i += 1
            elif self.hits[i] > hi:
                break
            else:
                count += 1
                i += 1
        return count 

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)