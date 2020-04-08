import collections

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hash_map = collections.defaultdict(list)
        short_hash_map = collections.defaultdict(list)        
        N = len(nums)
        for k in range(N):
            short_hash_map[nums[k]].append(k)
        
        shortened_nums = []
        for k,v in short_hash_map.items():
            cnt = 0
            for i in range(len(v)):
                if cnt < 3: 
                    shortened_nums.append(k)
                else:
                    break
                cnt += 1
        
        nums = shortened_nums
        N = len(nums)
        res = set()
        
        for k in range(N):
            hash_map[nums[k]].append(k)
        
        for i in range(N):
            for j in range(i+1,N): 
                if -(nums[i]+nums[j]) in hash_map:
                    for k in hash_map[-(nums[i]+nums[j])]:
                        if i != k and j != k: 
                            res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return list(res)
                        
