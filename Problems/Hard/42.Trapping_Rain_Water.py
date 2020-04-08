from sys import maxint as MAX_VAL

MAXVAL = MAX_VAL
MINVAL = -MAX_VAL-1
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        min_left = MINVAL 
        len_height = len(height)
        left = [0]*len_height
        right = [0]*len_height
        support_list = [0]*len_height
       
        for i in xrange(len_height):
            min_left = left[i] = max(min_left,height[i])
        
        min_right = MINVAL
        for i in xrange(len_height-1,0,-1):
            min_right = right[i] = max(min_right,height[i])
        
        total_trapped = 0
        for i in xrange(len_height):
            total_trapped +=  max(0, min(left[i],right[i])-height[i])
            
        return total_trapped
