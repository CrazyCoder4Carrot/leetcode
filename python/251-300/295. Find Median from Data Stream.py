import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heaps = [],[]
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(small) > len(large):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        small, large = self.heaps
        if len(small) < len(large):
            return float(large[0])
        return (-small[0] + large[0]) / 2.0
            

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()