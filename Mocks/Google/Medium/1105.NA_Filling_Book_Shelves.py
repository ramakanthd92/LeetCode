class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        B = len(books)
        dp = [[ [-1,-1,-1] for i in range(2)] for j in range(B)] 
        
        dp[0][0] = [0,books[0][1],books[0][0]]
            
        # [shelf_height, total_height, book_width]
        # same shelf
        # next shelf
        for i in range(1,B):
            # can fit the book in the same shelf
            if dp[i-1][0][2] != -1 and shelf_width-dp[i-1][0][2] <= books[i][0]:
                dp[i][0] = [dp[i-1][0][0],max(dp[i-1][0][0]+books[i][1],dp[i-1][0][1]),dp[i-1][0][2]-books[i][0]]
            # try to fit in the next shelf
                dp[i][1] = [dp[i-1][0][1],max(dp[i-1][0][0]+books[i][1],dp[i-1][0][1]),dp[i-1][0][2]-books[i][0]]
            else:
                dp[i][1] = [dp[i-1][1][0],max(dp[i-1][0][0]+books[i][1],dp[i-1][0][1]),dp[i-1][0][2]-books[i][0]]

