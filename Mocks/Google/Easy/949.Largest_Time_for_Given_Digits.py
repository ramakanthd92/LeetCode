class Solution(object):
    def __init__(self):
        self.res = []
        
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        
        def helper(A,i,N,used,path):
            if i > N:
                return 
            elif i == N:
                if ((path[0] <= 1) or \
                    (path[0] == 2 and path[1] <=3)) and \
                   (path[2] <= 5):
                    fpath = [str(p) for p in path] 
                    self.res.append("".join(fpath))
                
            for j in range(N):
                if not used[j]:
                    path[i] = A[j]
                    used[j] = True
                    helper(A,i+1,N,used,path)
                    used[j] = False
                    path[i] = -1 
        
        used = [False,False,False,False]
        path = [-1,-1,-1,-1]
        helper(A,0,4,used,path)
        
        #print self.res
        output = ""
        if len(self.res) > 0:
            self.res.sort()
            output = self.res[-1][0:2]+':'+self.res[-1][2:4]
        
        return output
        
