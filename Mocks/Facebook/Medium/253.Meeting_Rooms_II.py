class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start_int = []
        end_int = []
        
        for [s,e] in intervals:
            start_int.append(s)
            end_int.append(e)
        
        start_int.sort()
        end_int.sort()
        
        i = 0
        j = 0
        L = len(intervals)
        res = 0
        
        while (i < L):
            while(i < L and start_int[i] < end_int[j]):
                i += 1
            res = max(res, i-j)
            while(j < L and i < L and start_int[i] >= end_int[j]):
                j += 1
            res = max(res, i-j)
            
        return res
