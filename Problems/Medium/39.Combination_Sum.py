# Runtime - 140 ms    Memory 13.1 MB

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(candidates)
        res = set()
        def recurse(i,N,target,pathSum,path):
            if pathSum == target:
                res.add(tuple(sorted(path[:])))
                return 
            if i == N or pathSum > target:
                return 
            for j in range(i,N):
                path.append(candidates[j])
                recurse(j,N,target,pathSum+candidates[j],path)    
                path.pop()
                
        path = []
        recurse(0,N,target,0,path)
        
        return res
        
