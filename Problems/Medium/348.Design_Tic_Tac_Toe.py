# Runtime - 152 ms   Memory - 14.2 MB
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [[0 for _ in range(n)] for _ in range(n)] 
        self.grid_size = n
    
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        def check(row, col, player):
            # Check Horizontal
            h, v, ld, rd = True, True, False, False
            for i in range(0,self.grid_size):
                h = h and self.grid[row][i] == player
                
            # Check Vertical
            for i in range(0,self.grid_size):
                v = v and self.grid[i][col] == player
            
            if (row + col == self.grid_size-1):
                # Check Diagonally
                rd = True
                for i in range(0,self.grid_size):
                    rd = rd and self.grid[i][self.grid_size-1-i] == player
            
            if (row == col):
                # Check Diagonally
                ld = True
                for i in range(0,self.grid_size):
                    ld = ld and self.grid[i][i] == player
            #print h,v,ld,rd
            if (h or v or ld or rd):
                return player
            return 0
        
        if not self.grid[row][col]:
            self.grid[row][col] = player
            #print self.grid
            return check(row,col,player)
        else:
            return -1

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
