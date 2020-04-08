import collections
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        
        hash_map = collections.defaultdict()
        L = len(dominoes)
        for i in range(L):
            if dominoes[i][0] == dominoes[i][1]:
                s = b = dominoes[i][0]
            elif dominoes[i][0] > dominoes[i][1]:
                s = dominoes[i][1] 
                b = dominoes[i][0] 
            elif dominoes[i][0] < dominoes[i][1]:
                s = dominoes[i][0] 
                b = dominoes[i][1] 
    
            if (s,b) not in hash_map:
                hash_map[(s,b)] = 1
            else:
                hash_map[(s,b)] += 1
        pairs = 0
        for k,v in hash_map.items():
            pairs +=  (v*(v-1))/2
        
        return pairs
