# Runtime - 44 ms  Memory - 13.2 MB

class Solution(object):
    def longestValidParentheses(self, A):
        """
        :type s: str
        :rtype: int
        """
        l = len(A)
        if l == 0:
	        return 0
	        
        stk = collections.deque()
        for i in range(l):
            if (A[i] == '('):
                stk.append(i)
            elif (A[i] == ')'):
                size = len(stk)
                if size-1 >= 0  and stk[size-1] < len(A) and A[stk[size-1]] == '(':
                    stk.pop()
                else:
                    stk.append(i)
        
        max_length = 0
        stk_len = len(stk)
        last_index = len(A)
        
        for _ in range(stk_len):
            curr_index = stk.pop()
            max_length = max(max_length,last_index-curr_index-1)
            last_index = curr_index
        
        curr_index = -1
        max_length = max(max_length,last_index-curr_index-1)
        
        return max_length
