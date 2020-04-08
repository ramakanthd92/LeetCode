# Runtime-  60 ms   Memory - 15.2 MB
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        N = len(intervals)
        start_times = []
        end_times = []
        for i in range(N):
            start_times.append(intervals[i][0])
            end_times.append(intervals[i][1])
            
        start_times.sort()
        end_times.sort()
        
        s = 0
        e = 0
        
        rooms = 0
        while(s < N and e < N):
            while(s < N and start_times[s] < end_times[e]):
                rooms = max(s-e+1,rooms)
                s += 1
            e += 1
            
        return rooms
            
            
