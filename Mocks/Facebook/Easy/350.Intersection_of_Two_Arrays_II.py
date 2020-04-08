import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        first_hash_map = collections.defaultdict(int)
        second_hash_map = collections.defaultdict(int)
        
        for n in nums1:
            first_hash_map[n] += 1
            
        for n in nums2:
            second_hash_map[n] += 1
            
        res = []
        for fk,fv in first_hash_map.items():
            if fk in second_hash_map:
                res += [fk for _ in range(min(fv,second_hash_map[fk]))]
        
        return res
            
