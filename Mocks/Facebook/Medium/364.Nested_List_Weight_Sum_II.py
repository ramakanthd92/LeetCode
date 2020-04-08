import collections

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        level_sum = 0
        total_level = 0
        hash_map = collections.defaultdict(int)
        total_level = 0
        
        def helper(list_item,level):    
            child_lists = 0
            child_lists = len(list_item)
            
            for i in range(child_lists):
                val = list_item[i].getInteger() # is Integer
               # print 
                if val:   
                    hash_map[level] += val
                else:
                    helper(list_item[i].getList(),level+1)
                
        helper(nestedList,1)
        #print hash_map
        
        if hash_map.keys():
            total_level = max(hash_map.keys())
            
        for k,v in hash_map.items():
            #print v,total_level,k
            level_sum += v*(total_level-k+1)
        
        return level_sum
