import collections

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map = collections.defaultdict(list) 
        cum_sum = 0
        hash_map[0].append(-1)
        max_len = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            hash_map[cum_sum].append(i)
            if cum_sum-k in hash_map:
                for j in hash_map[cum_sum-k]:
                    max_len = max(max_len,i-j)
            
       # print hash_map
        return max_len
