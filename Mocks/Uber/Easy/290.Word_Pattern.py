import collections
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not len(str) and not len(pattern):
            return True
        if not len(str) or not len(pattern):
            return False
            
        str_list = str.split(' ')
        
        if len(str_list) != len(pattern):
            return False
        
        hash_map = collections.defaultdict(set)
        hash_map_2 = collections.defaultdict(set)
        
        for i in range(len(pattern)):
            hash_map[pattern[i]].add(str_list[i])
            hash_map_2[str_list[i]].add(pattern[i])
        
        for k,v in hash_map.items():
            if len(v) > 1:
                return False
            
        for k,v in hash_map_2.items():
            if len(v) > 1:
                return False
        
        return True
