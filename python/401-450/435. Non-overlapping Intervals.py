# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import sys
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        earase = 0
        end = -sys.maxint
        intervals.sort(key = lambda interval: interval.end)
        for interval in intervals:
            if interval.start >= end:
                end = interval.end
            else:
                earase += 1
        return earase
            
            
            
        