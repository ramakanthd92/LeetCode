import collections

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if len(S) == 0:
            return [0]
        
        def takeFirst(elem):
            return elem[0]
        output = []
        def merge_intervals():
            ranges.sort(key=takeFirst)
            range_len = len(ranges)
            min_range = 0
            max_range = 0
            for i in range(len(ranges)):
                #print i
                if ranges[i][0] > max_range:
                    output.append([min_range,max_range])
                    min_range = ranges[i][0]
                    max_range = ranges[i][1]
                max_range = max(ranges[i][1],max_range)
            output.append([min_range,max_range])
            
        hash_map = collections.defaultdict(list)
        
        for i,c in enumerate(S):
            if c not in hash_map:
                hash_map[c] = [i,i]
            else:
                hash_map[c][1] = i
        
        ranges = []
        
        for k,v in hash_map.items():
            ranges.append(v)
            
            
        merge_intervals()
        
        #print ranges
        #print output
        
        res = []
        for [a,b] in output:
            res.append(b-a+1)
        
        return res
