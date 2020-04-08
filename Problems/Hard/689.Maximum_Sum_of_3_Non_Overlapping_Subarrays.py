# Runtime -8260 ms    Memory - 41.7 MB
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        N = len(nums)
        dp = [[[0,set()] for i in range(N+1)]for l in range(4)]
        
        for l in range(1,4):
            for i in range(k,N+1):
                if dp[l-1][i-k][0] + sum(nums[i-k:i]) > dp[l][i-1][0]:                
                    dp[l][i][0] = dp[l-1][i-k][0]+sum(nums[i-k:i])
                    new_set = set()
                    if not dp[l-1][i-k][1]:
                        new_set.add(i-k)
                    else:
                        new_set = new_set.union(dp[l-1][i-k][1])
                        new_set.add(i-k)
                    dp[l][i][1] = new_set
                else:
                    dp[l][i][0] = dp[l][i-1][0]            
                    dp[l][i][1] = dp[l][i-1][1]             
            
#         for i in range(4):
#             res  = []
#             for j in range(N):
#                 res.append(dp[i][j])
#             print res

        max_val = 0
        output = 0
        for i in range(N+1):
            if dp[3][i][0] > max_val:
                max_val = dp[3][i][0]
                output = dp[3][i][1]
           # print i,max_val,output
            
        #print dp
        if len(output) == 3:
            return sorted(output)
        return []
        return dp[3][N-1][1]

