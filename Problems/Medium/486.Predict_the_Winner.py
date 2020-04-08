# Runtime - 24 ms  Memory - 11.9 MB

class Solution(object):
    def PredictTheWinner(self, arr):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
       # Create a table to store  
        # solutions of subproblems 
        n = len(arr)
        table = [[0 for i in range(n)] 
                for i in range(n)] 
  
    # Fill table using above recursive  
    # formula. Note that the table is  
    # filled in diagonal fashion  
    # (similar to http://goo.gl/PQqoS), 
    # from diagonal elements to 
    # table[0][n-1] which is the result.  
        for gap in range(n): 
            for j in range(gap, n): 
                i = j - gap 
                print i,j
            # Here x is value of F(i+2, j),  
            # y is F(i+1, j-1) and z is  
            # F(i, j-2) in above recursive  
            # formula  
                x = 0
                if((i + 2) <= j): 
                    x = table[i + 2][j] 
                y = 0
                if((i + 1) <= (j - 1)): 
                    y = table[i + 1][j - 1] 
                z = 0
                if(i <= (j - 2)): 
                    z = table[i][j - 2] 
                table[i][j] = max(arr[i] + min(x, y), 
                                  arr[j] + min(y, z)) 
        #print table[0][n - 1] 
        
        total_sum = 0
        for i in range(n):
            total_sum += arr[i]
            
        if table[0][n-1] >= total_sum - table[0][n-1]:
            return True
        
        return False
                    
