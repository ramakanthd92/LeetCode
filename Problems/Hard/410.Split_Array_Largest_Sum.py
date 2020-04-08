#import sys.maxint as MAX_VAL
# Runtime - 4444 ms   Memory - 12 MB
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        MAX_VAL = float('inf')
        n = len(nums)
        LCS = [[MAX_VAL for i in range(m)] for j in range(n)]
        
        for j in range(0,m):
           # print LCS
            sum_0_i = 0
            for i in range(j,n):
                if j == 0:
                    sum_0_i += nums[i]
                    LCS[i][j] = sum_0_i
                else:
                    sum_k1_i = sum(nums[0:i+1])
                    for k in range(0,i+1):       
                       # print i,j,k, LCS[i][j] , k,j-1, LCS[k][j-1],nums[k+1:i+1] ,sum(nums[k:i])          sum_k+1+i = 0 +
                        sum_k1_i -= nums[k] 
                        LCS[i][j] = min(max(LCS[k][j-1],sum_k1_i),LCS[i][j])                         
                     #   print LCS[i][j]
    #    print LCS
        
        return LCS[n-1][m-1]
