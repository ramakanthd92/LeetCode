import collections

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window_sum = 0 
        self.window_size = size
        self.window_dq = collections.deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.window_size == 0:
            return 0
        
        if len(self.window_dq) < self.window_size:
            self.window_dq.append(val)
            self.window_sum += val
            return (self.window_sum / float(len(self.window_dq)))
        elif len(self.window_dq) == self.window_size:
            dq_front = self.window_dq.popleft()
            self.window_sum -= dq_front
            self.window_dq.append(val)
            self.window_sum += val
            return (self.window_sum / float(len(self.window_dq)))
            
