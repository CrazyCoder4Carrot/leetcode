class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.x = 0
        self.y = 0

    def next(self):
        """
        :rtype: int
        """
        temp = self.vec2d[self.x][self.y]
        if self.y + 1 < len(self.vec2d[self.x]):
            self.y += 1
        else:
            self.x += 1
            self.y = 0
        #print temp
        return temp
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.x < len(self.vec2d) and len(self.vec2d[self.x]) == 0:
            self.x += 1
        if self.x == len(self.vec2d):
            return False
        if self.y < len(self.vec2d[self.x]):
            return True
        else:
            while self.x < len(self.vec2d) and len(self.vec2d[self.x]) == 0:
                self.x += 1
            if self.x < len(self.vec2d):
                return True
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())