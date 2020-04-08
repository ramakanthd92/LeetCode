class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        squares = []
        
        for i in A:
            squares.append(i*i)
            
        squares.sort()
        
        return squares
