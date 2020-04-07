#Runtime - 76 ms   Memory - 14.9 MB

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(intervals)
        if N <= 1:
            return intervals
        intervals.sort()
        
        start,end = intervals[0][0],intervals[0][1]
        res = []
        i = 0
        while (i < N-1):
            if intervals[i+1][0] > max(end,intervals[i][1]):
                end = max(end,intervals[i][1])
                res.append([start,end])
                start = intervals[i+1][0]
            else:
                end = max(intervals[i][1], end)
            i += 1
        end = max(intervals[i][1], end)
        res.append([start,end])
        
        return res
