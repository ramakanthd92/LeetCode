#Runtime - 60 ms   Memory - 15.7 MB

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = list()
        self.stack = list()
        self.count = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.min_stack) > 0:
            if self.stack[self.min_stack[-1]] > x:
                self.min_stack.append(self.count)
        else:
            self.min_stack.append(self.count)
        self.count += 1
        #print self.stack, self.min_stack, self.count
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if len(self.min_stack) > 0:
            if self.min_stack[-1] >= self.count-1:
                self.min_stack.pop()
        self.count -= 1
    
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        return "NA"

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) > 0:
            return self.stack[self.min_stack[-1]]
        return "NA"

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
