import heapq
import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        
        # Heap
        # Dictionary
        # Stack 
        
        hash_map = collections.defaultdict(int)
        pos_hash_map = collections.defaultdict(int)
        
        N = len(tasks)
        for i in range(N):
            hash_map[tasks[i]] += 1
        
        task_list = []
        stack = []
        
        for k,v in hash_map.items():
            heapq.heappush(task_list,[v,k])
        
        i = 0
        while(len(task_list) > 0 or len(stack) > 0):
            if len(task_list) > 0:
                count,val = heapq.heappop(task_list)
                print count,val                    
                if val not in pos_hash_map or n > (i - pos_hash_map[val]):
                    pos_hash_map[val] = i 
                    i += 1
                    count -= 1
                    if count > 0:
                        heapq.heappush(task_list,(count,val))    
                    while(len(stack) > 0):
                        c,v = stack.pop()
                        heapq.heappush(task_list,(c,v))  
                stack.append((count,val))
            else:
                i += 1
                print "idle"
                while(len(stack) > 0):
                    c,v = stack.pop()
                    heapq.heappush(task_list,(c,v))
        
        return i
