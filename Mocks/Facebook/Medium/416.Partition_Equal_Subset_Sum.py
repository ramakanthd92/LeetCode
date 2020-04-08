class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cum_sum = sum(nums)
        
        if cum_sum % 2:
            return False
        
        subset_sum =  cum_sum/2
                        
        max_val = 0
        dp = [False for i in range(20000)]
        dp[0] = True
        N = len(nums)
        for i in range(N):
            #print dp[:20]
            hash_arr = []
            for j in range(min(max_val,subset_sum)+1):
                if dp[j] and j + nums[i] == subset_sum:
                    #print dp[j], j, nums[i],i,subset_sum
                    return True
                if dp[j]: 
                    hash_arr.append(nums[i]+j)
                    max_val = max(max_val,nums[i]+j)
            for k in hash_arr:
                dp[k] = True
            dp[nums[i]] = True 
            max_val = max(max_val,nums[i])
        return False
