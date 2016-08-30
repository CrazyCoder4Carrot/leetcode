import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            print pair
            for a, b in zip(*pair):
                print a, b
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set("".join(words))
        free = chars - set(pre)
        order = ""
        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)
        return order * (set(order) == chars)
sol = Solution()
temp = ["wrt","wrf","er","ett","rftt"]
sol.alienOrder(temp)