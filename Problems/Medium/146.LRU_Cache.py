#Runtime - 7584 ms Memory - 21.1 MB

import collections
import heapq

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.entry_map = collections.defaultdict() 
        self.L = []
        self.counter = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.entry_map:
            entry = self.entry_map[key]
            entry[0] = self.counter
            self.counter += 1
            heapq.heapify(self.L)
            return self.entry_map[key][2]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.L) < self.capacity:
            if key not in self.entry_map:
                entry = [self.counter,key,value]
                self.entry_map[key] = entry
                heapq.heappush(self.L, entry)
                self.counter += 1
            else:
                entry = self.entry_map[key] 
                entry[0] = self.counter
                entry[2] = value
                heapq.heapify(self.L)
                self.counter += 1
        else:
            if key not in self.entry_map:
                entry = [self.counter,key,value]
                elem = heapq.heappop(self.L)
                del self.entry_map[elem[1]]
                self.entry_map[key] = entry
                heapq.heappush(self.L, entry)
                self.counter += 1
            else:
                entry = self.entry_map[key] 
                entry[0] = self.counter
                entry[2] = value
                heapq.heapify(self.L)
                self.counter += 1
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
