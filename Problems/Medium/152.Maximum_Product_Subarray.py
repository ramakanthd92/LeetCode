# Runtime - 48 ms   Memory - 12.9 MB

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
#         N = len(nums)
#         if not N:
#             return 0
        
#         prod_arr = [[0 for i in range(N)] for j in range(N)]
#         max_prod = -float("inf")
        
#         for k in range(N):
#             for i in range(N):
#                 if k == 0:
#                     prod_arr[i][i] = nums[i]
#                     max_prod = max(max_prod,prod_arr[i][i])
#                 else:
#                     if (i >= k):
#                         prod_arr[i-k][i] = prod_arr[i-k][i-1]*nums[i]
#                         max_prod = max(max_prod,prod_arr[i-k][i])

        neg,pos = -float("inf"),-float("inf")
    
        N = len(nums)
        if not N:
            return 0

        max_prod = -float("inf")
        
        i = 0
        while (i<N):
            if nums[i] == 0:
                neg, pos = 0,0
            elif nums[i] > 0:
                pos,neg = pos*nums[i], neg*nums[i]
                pos = max(pos,nums[i])
                
            else: # negative number
                neg,pos = pos*nums[i], neg*nums[i]
                neg = min(neg,nums[i])
            if pos == float('inf'):
                pos = -float("inf")
            if neg == float('inf'):
                neg = -float("inf")
                
            max_prod = max(max(neg,pos),max_prod)    
           # print i,pos,neg
            i+=1
            
        return max_prod
