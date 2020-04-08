import collections

class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        
        hash_map = collections.defaultdict()
        
        for a in arr1:
            if a not in hash_map:
                hash_map[a] = 0
            else:
                hash_map[a] += 1
       
        for a in arr2:
            if a not in hash_map:
                hash_map[a] = 0
            else:
                hash_map[a] += 1
        
        for a in arr3:
            if a not in hash_map:
                hash_map[a] = 0
            else:
                hash_map[a] += 1
                
        res = []
        
        #print hash_map
        
        for k,v in hash_map.items():
            if v == 2:
                res.append(k)
        
        return res
