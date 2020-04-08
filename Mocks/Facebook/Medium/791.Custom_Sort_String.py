import collections

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        hash_map = collections.defaultdict(int)
        
        rest_string = ""
        for i in T:
            hash_map[i] += 1
            if i not in S:
                rest_string += i
            
        res = []
        for j in S:
            res.append(j*hash_map[j])
            
        res += rest_string
        
        return "".join(res)
        
