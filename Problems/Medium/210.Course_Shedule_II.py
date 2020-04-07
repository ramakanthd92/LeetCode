# Runtime - 80 ms   Memory - 13.5 MB
import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        adj_list = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        
        N = len(prerequisites)
        
        for i in range(N):
            adj_list[prerequisites[i][1]].append(prerequisites[i][0])
            in_degree[prerequisites[i][0]] += 1
        
        num_set = set() 
        
        for i in range(numCourses):
            num_set.add(i)
        
        start_courses = num_set.difference(set(in_degree.keys()))
        
        queue = deque()
        for s in start_courses:
            queue.append(s)
        
        res = []
        visited = [False for i in range(numCourses)]
        
        while (len(queue) > 0):
            course = queue.popleft() 
            res.append(course)
            for adj_course in adj_list[course]:
                in_degree[adj_course] -= 1
                if in_degree[adj_course] == 0:
                    queue.append(adj_course)
        
        if len(res) != numCourses: 
            return []
        return res
        
