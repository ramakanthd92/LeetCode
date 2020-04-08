import collections

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash_map = collections.defaultdict()
            
        for (i,l) in enumerate(s):
            if l == 'A':
                if l not in hash_map:
                    hash_map[l] = 1
                else:
                    hash_map[l] += 1  
                if 'L' in hash_map and hash_map['L'] <= 2:
                    hash_map['L'] = 0    
            elif l == 'L':
                if l not in hash_map:
                    hash_map[l] = 1
                else:
                    hash_map[l] += 1
            else:
                 if 'L' in hash_map and hash_map['L'] <= 2:
                    hash_map['L'] = 0
        
        #print hash_map
        
        if 'A' in hash_map and hash_map['A'] > 1:
            return False
        elif 'L' in  hash_map and hash_map['L'] > 2:
            return False
        return True
