# Runtime - 52 ms   Memory - 16.2 MB

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        N = len(intervals)
        
        if N == 0 and not newInterval:
            return []
        if N == 0 and newInterval:
            return [newInterval]
        
        s = newInterval[0]
        e = newInterval[1]
        
        res = []
        
        i = 0
        while (i < N and s > intervals[i][1]):
            res.append(intervals[i])
            i += 1
            
        j = i
       # print i,j
        
        while (j < N and e >= intervals[j][0]):
            j += 1
        
        max_end = -1
        if j-1 >= 0:
            max_end = intervals[j-1][1] 
        
            
        min_start = float("inf")
        if i < N:
            min_start = intervals[i][0] 
        
        res.append([min(min_start,s), max(max_end,e)])
         
        #print i,j
        while(j < N):
            if j < N:
                res.append(intervals[j]) 
            j += 1
        
        return res
        
