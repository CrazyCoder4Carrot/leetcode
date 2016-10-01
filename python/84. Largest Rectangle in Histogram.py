class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        right = [1] * n
        left = [1] * n
        for i in range(n-2, -1, -1):
        	if heights[i] > heights [i + 1]:
        		continue
        	else:
        		j = i + 1
        		while j < n and heights[i] <= heights[j]:
        			j += right[j]
        		right[i] = j - i
        for i in range(1, n):
        	if heights[i] < heights[i-1]:
        		continue
        	else:
        		j = i - 1
        		while j >= 0 and heights[i] <= heights[j]:
        			j -= left[j]
        		left[i] = i - j
        res = 0
        for i in range(n):
        	res = max(res, heights[i] * (left[i] + right[i] - 1))
        return res
    # using stack
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res
                