import heapq


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x.start, x.end))
        count = 0
        visit = [False] * len(intervals)
        for i in range(len(intervals)):
            if visit[i]:
                continue
            count += 1
            visit[i] = True
            end = intervals[i].end
            for j in range(i + 1, len(intervals)):
                if visit[j]:
                    continue
                if end <= intervals[j].start:
                    end = intervals[j].end
                    visit[j] = True
        return count
