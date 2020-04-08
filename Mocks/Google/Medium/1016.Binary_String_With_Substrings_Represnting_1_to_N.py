class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        def dec_to_bin(num):
            num_str = ""
            val = num
            while (num):
                if num%2:
                    num_str = '1' + num_str
                else:
                    num_str = '0' + num_str
                num = num/2
            #print val,num_str
            return num_str
            
        
#         def binary_to_dec(sub_str): 
#             rev_str = sub_str[::-1] 
#             len_str = len(rev_str)
#             i = 0
#             x = 0
#             while(i < len_str):
#                 if rev_str[i] == '1':
#                     x = x + pow(2,i)   
#                 i += 1    
#             return x
        
#         M = N
#         k = 0
#         while(M):
#             M = M/2
#             k += 1
#         len_str = len(S)
                
#         dec_arr = [False]*pow(2,k)
        
#         for x in range(1,k):
#             for j in range(len_str):
#                 if j+x <= len_str:
#                     y =  binary_to_dec(S[j:j+x])
#                     dec_arr[y] = True
    
#         #print dec_arr 
        
        i = 1    
        while i <= N:
            if dec_to_bin(i) not in S:
                return False
            i+=1
            
        return True
        
