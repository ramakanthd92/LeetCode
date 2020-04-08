#Runtime - 256 ns  Memory -  25.4 MB

import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low_heap = []    # Max Heap
        self.high_heap = []   # Min Heap
        self.size = 0
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        low_heap_top = -float('inf')
        high_heap_top = float('inf')
        if len(self.low_heap) > 0:
            low_heap_top = self.low_heap[0][1]
        if len(self.high_heap) > 0:
            high_heap_top = self.high_heap[0][1]
       
        if len(self.low_heap) < len(self.high_heap):
            if num < high_heap_top:
                heapq.heappush(self.low_heap,[-1*num,num])
            else:
                high_pop = heapq.heappop(self.high_heap)
                heapq.heappush(self.low_heap,[-1*high_pop[1],high_pop[1]])
                heapq.heappush(self.high_heap,[num,num])
                                          
        elif len(self.low_heap) > len(self.high_heap):
            if num > low_heap_top:
                heapq.heappush(self.high_heap,[num,num])  
            else:
                low_pop = heapq.heappop(self.low_heap)
                heapq.heappush(self.high_heap,[low_pop[1],low_pop[1]])
                heapq.heappush(self.low_heap,[-1*num,num])
                                         
        elif len(self.low_heap) == len(self.high_heap):
            if low_heap_top > num and low_heap_top != -float('inf'):
                heapq.heappush(self.low_heap,[-1*num,num])
            else:
                heapq.heappush(self.high_heap,[num,num])
        self.size += 1 

    def findMedian(self):
        """
        :rtype: float
        """
        if self.size == 0:
            return 0
        elif self.size == 1:
            if len(self.low_heap) < len(self.high_heap):
                return self.high_heap[0][1]
            else:
                return self.low_heap[0][1]   
        elif self.size % 2 == 0 :
            return (self.low_heap[0][1] + self.high_heap[0][1])/2.0
        elif self.size % 2 != 0:
            if len(self.low_heap) > len(self.high_heap):                      
                return self.low_heap[0][1]
            else:
                return self.high_heap[0][1]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
