import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        routes = collections.defaultdict(list)
        visited = collections.defaultdict(int)
        for s, e in sorted(tickets):
            routes[s].append(e)
            visited[(s, e)] += 1
        n = len(tickets) + 1
        self.path = ['JFK']
        def dfs(cur, n):
            if len(self.path) == n:
                return True
            for end in routes[cur]:
                if visited[(cur, end)] > 0:
                    visited[(cur, end)] -= 1
                    self.path.append(end)
                    if dfs(end, n):
                        return True
                    self.path = self.path[:-1]
                    visited[(cur, end)] += 1
        dfs("JFK", n)
        return self.path


tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
sol = Solution()
print sol.findItinerary(tickets)