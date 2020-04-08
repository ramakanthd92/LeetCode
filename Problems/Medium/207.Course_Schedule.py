# Runtime - 92 ms   Memory - 13.4 MB

import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        L = [] 
        S = set()
        adj_list = collections.defaultdict(list)
        incoming = collections.defaultdict(list)
        
        for i in xrange(numCourses):
            S.add(i)
        
        for pre in prerequisites:
            adj_list[pre[0]].append(pre[1])
            if pre[1] in S:
                S.remove(pre[1])
            incoming[pre[1]].append(pre[0])
        
        while (len(S) > 0):
            node = S.pop()
            neighbours = adj_list[node][:]
            for n in neighbours:
                adj_list[node].remove(n)
                incoming[n].remove(node)
                if len(incoming[n]) == 0:
                    S.add(n)
            L.append(node)
        #print L
        for i in xrange(numCourses):
            if len(adj_list[i]) > 0:
                return False
        return True
