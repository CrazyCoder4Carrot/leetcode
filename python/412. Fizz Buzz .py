class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [str(i) for i in range(1, n+1)]
        for i in range(1, n/3 + 1):
            res[i*3-1] = "Fizz"
        for i in range(1, n/5 + 1):
            res[i*5-1] = "Buzz"
        for i in range(1, n/15 + 1):
            res[i*15-1] = "FizzBuzz"
        return res