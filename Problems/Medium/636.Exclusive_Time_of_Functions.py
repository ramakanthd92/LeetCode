#Runtime - 284 ms    Memory - 12.9 MB

import collections

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        def read_values(s):
            s_word = s.split(':')
            return int(s_word[0]),s_word[1],int(s_word[2])
        start_hash_map = collections.defaultdict(int)
        hash_map = collections.defaultdict(int)
        stack = list()
        count = 0
        
        time_stack = []
        mod_logs = []
        process_hash_map= collections.defaultdict(list)
        process_cnt = 0
        for s in logs:
            pid,marker,time = read_values(s)
            if marker == "start":
                time_stack.append([process_cnt,"start",time])
                process_hash_map[pid].append(process_cnt)
                mod_logs.append(str(process_cnt)+":"+"start"+":"+str(time))
                process_cnt += 1

            else:
                p,m,t = time_stack.pop()
                mod_logs.append(str(p)+":"+"end"+":"+str(time))
            
        logs = mod_logs
        
       #print mod_logs
                
        for s in logs:
            pid,marker,time = read_values(s)
            if marker == "start":
                stack.append((pid,time))
                start_hash_map[time] = [pid,None]
            else:
                #print stack,hash_map
                if stack[-1][0] == pid:
                    diff = time-stack[-1][1]+1
                    #print time, stack[-1][1], diff
                    hash_map[pid] += diff
                    for k in start_hash_map.keys():
                        past_ps = start_hash_map[k]
                        if k < time and past_ps[1] == None and past_ps[0] != pid:
                            hash_map[past_ps[0]] -= hash_map[pid]
                        elif past_ps[0] == pid:
                            past_ps[1]= time
                    stack.pop()
            
        res = []
        #print hash_map
       # print process_hash_map
        for k in sorted(process_hash_map.keys()):
            time_count = 0
            for j in process_hash_map[k]:
                time_count += hash_map[j]
            res.append(time_count)
            
        return res
    
    
#     0  1 2 6
#     10 5 4 9
    
#       0 10
#     1 5  6 9
#     2 4
