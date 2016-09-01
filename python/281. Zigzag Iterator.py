class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = [_ for _ in (v1, v2) if _]
        

    def next(self):
        """
        :rtype: int
        """
        v = self.queue.pop(0)
        ret = v.pop(0)
        if v:
            self.queue.append(v)
        return ret
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.queue:
            return True
        return False