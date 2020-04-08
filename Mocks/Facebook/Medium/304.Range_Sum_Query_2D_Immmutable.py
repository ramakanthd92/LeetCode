class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.row_len = len(matrix)
        if len(matrix) > 0:
            self.col_len = len(matrix[0])
            self.preProcess()
    
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total_sum = 0
        for i in range(col1,col2+1):
            if row1 > 0:
                total_sum += (self.matrix[row2][i]-self.matrix[row1-1][i])
            else:
                total_sum += self.matrix[row2][i]
        return total_sum        
        
    def preProcess(self):
        
        for j in range(self.col_len):
            cum_sum = 0
            for i in range(self.row_len):
                cum_sum += self.matrix[i][j]
                self.matrix[i][j] = cum_sum
        print self.matrix
                

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
