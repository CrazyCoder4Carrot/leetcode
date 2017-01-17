class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        start = 0
        end = n - 1
        max_area = min(height[start], height[end]) * (end - start)
        while end > start:
            if height[end] >= height[start]:
                start += 1
            elif height[end] < height[start]:
                end -= 1
            max_area = max(max_area, min(height[start], height[end]) * (end - start))
        return max_area