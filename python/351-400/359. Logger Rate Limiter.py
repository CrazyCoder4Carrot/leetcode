class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.dic:
            self.dic[message] = timestamp
            return True
        else:
            if timestamp - self.dic[message] >= 10:
                self.dic[message] = timestamp
                return True
            else:
                return False