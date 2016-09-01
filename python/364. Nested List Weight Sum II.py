class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        unweight = weight = 0
        while nestedList:
            nextlevel = []
            for temp in nestedList:
                if temp.isInteger():
                    unweight += temp.getInteger()
                else:
                    nextlevel += temp.getList()
            weight += unweight
            nestedList = nextlevel
        return weight
        