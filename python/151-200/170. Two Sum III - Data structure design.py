class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.temp = {}
    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number not in self.temp:
            self.temp[number] = 1
        else:
            self.temp[number] += 1
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for v in self.temp:
            if value - v in self.temp and (value - v != v or self.temp[v] > 1):
                return True
        return False