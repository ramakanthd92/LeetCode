import collections

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        hash_map = collections.defaultdict()
        
        for n in set1:
            if n not in hash_map:
                hash_map[n] = 0
            else:
                hash_map[n] += 1
        
        for n in set2:
            if n not in hash_map:
                hash_map[n] = 0
            else:
                hash_map[n] += 1
        
        res = []
        for k,v in hash_map.items():
            if v == 1:
                res.append(k)
            
        return res
