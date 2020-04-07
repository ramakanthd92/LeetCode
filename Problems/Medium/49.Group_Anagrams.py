# Runtime - 152 ms  Memory - 17.4 MB 

import collections  

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = collections.defaultdict(list)
        
        if not len(strs):
            return []
        for s in strs:
            hash_map["".join(sorted(s))].append(s)
        res = []
        for k,v  in hash_map.items():
            res.append(v)
        
        return res
