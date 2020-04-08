class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
                
        hash_map = collections.defaultdict(list)
        
        def helper(M):
            #print M
            if M == 0:
                return ['']
            if M == 1:
                return ['1','0','8', '5', '6', '9' ,'2']
            
            if M in hash_map:
                return hash_map[M]
            
            r = helper(M-2)
            
            res = set()
                
            for k in r:
                res.add('2'+k+'2') 
                res.add('2'+k+'5') 
                res.add('2'+k+'6')    
                res.add('2'+k+'9')  
                res.add('2'+k+'0')
                res.add('2'+k+'1')
                res.add('2'+k+'8')
                
                res.add('5'+k+'5')    
                res.add('5'+k+'2')    
                res.add('5'+k+'6')    
                res.add('5'+k+'9')  
                res.add('5'+k+'0')
                res.add('5'+k+'1')
                res.add('5'+k+'8')
                
                
                res.add('6'+k+'5')    
                res.add('6'+k+'2')    
                res.add('6'+k+'6')    
                res.add('6'+k+'9')  
                res.add('6'+k+'0')
                res.add('6'+k+'1')
                res.add('6'+k+'8')
                
                res.add('9'+k+'5')    
                res.add('9'+k+'2')    
                res.add('9'+k+'6')    
                res.add('9'+k+'9')  
                res.add('9'+k+'0')
                res.add('9'+k+'1')
                res.add('9'+k+'8')
                
                
                res.add('1'+k+'5')    
                res.add('1'+k+'2')    
                res.add('1'+k+'6')    
                res.add('1'+k+'9') 
                
                res.add('8'+k+'5')    
                res.add('8'+k+'2')    
                res.add('8'+k+'6')    
                res.add('8'+k+'9') 
                
                if N%2:
                    
                    if '2' in k or '5' in k or '6' in k or '9' in k:
                        res.add('1'+k+'0')
                        res.add('1'+k+'8')
                        res.add('1'+k+'1')
                
                        res.add('8'+k+'0')
                        res.add('8'+k+'8')
                        res.add('8'+k+'1')
                
            hash_map[M] = res
                
            return res
                    
        #helper(0)
        
        k = 0
        R = N
        while(R):
            R = R/10
            k+=1
        
        output = set()
        output.add('2')
        output.add('5')
        output.add('6')
        output.add('9')
        
        
        for i in range(1,k+1):
            #print i
            output = output.union(helper(i+1))
            
        #print output
        
        count = 0
        
        nums = [int(r) for r in output]
        
        nums.sort()
        
       # print res
        #print len(nums)
        
        #print nums[-1]
        
        #print N, len(nums)
        
        #print nums[0:10]
