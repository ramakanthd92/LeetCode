# Runtime - 92 ms    Memory - 13 MB

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_height = len(height)
        start = 0
        end = len_height-1
        max_area = 0 
        while start < end:
            area = min(height[start],height[end])*(end-start)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            if max_area < area:
                max_area = area
        return max_area
