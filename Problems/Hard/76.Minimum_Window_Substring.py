#Runtime - 80 ms  Memory - 15.5 MB

import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_map = collections.defaultdict() 
        target_map = collections.defaultdict() 
        N = len(s)
        formed = True
        
        t_count = 0
        for i in range(len(t)):
            if t[i] not in target_map:
                target_map[t[i]] = 1
            else:
                target_map[t[i]] += 1
          
        t_count = len(target_map.keys())
            
        min_window = ""
        start,end = 0,0
        
        s_count = 0
        for i in range(N):
            if s[i] not in hash_map:
                hash_map[s[i]] = 1
            else:
                hash_map[s[i]] += 1
            end = i
            
            if s[i] in target_map and target_map[s[i]] == hash_map[s[i]]:
                s_count += 1           
            
            while(start < N and s_count == t_count):
                if min_window == "" or end-start < len(min_window):
                    min_window = s[start:end+1]
                hash_map[s[start]] -= 1   
                if s[start] in target_map and target_map[s[start]] > hash_map[s[start]]:
                     s_count -= 1 
                start += 1
                
                
        return min_window
            
