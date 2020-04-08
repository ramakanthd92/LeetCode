import collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        hash_map = collections.defaultdict(list)
        N = len(nums)
        
        cum_sum = 0
        
        hash_map[cum_sum].append(-1)
        
        count = 0
        for i in range(N):
            cum_sum += nums[i]
            if cum_sum-k in hash_map:
                count += len(hash_map[cum_sum-k])
            hash_map[cum_sum].append(i)
            
        
        return count
        
