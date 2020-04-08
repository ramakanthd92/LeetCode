class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        [x1,y1,x2,y2] = rec1
        [x3,y3,x4,y4] = rec2
        
       # print x1,y1,x2,y2,x3,y3,x4,y4
        if (x2 <= x3 or x4 <= x1):
            return False
        
        if (y2 <= y3 or y4 <= y1):
            return False
        
        return True
        
        
