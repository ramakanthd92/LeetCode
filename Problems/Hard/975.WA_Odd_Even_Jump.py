class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        L = len(A)
        
     
        def compute_greatest_elems(A):
            greater_stk = []
            greater_arr = [None for i in range(L)]
            for i in range(L):
                while(len(greater_stk) > 0 and \
                        A[greater_stk[-1]] < A[i]):
                    greater_arr[greater_stk[-1]] = i
                    greater_stk.pop()
                greater_stk.append(i)
            return greater_arr
                        
        def compute_smallest_elems(A):
            smallest_stk = []
            smallest_arr = [None for i in range(L)]
            for i in range(L):
                while(len(smallest_stk) > 0 and \
                      A[smallest_stk[-1]] > A[i]):                             
                    smallest_arr[smallest_stk[-1]] = i
                    smallest_stk.pop()
                smallest_stk.append(i)
            return smallest_arr
        
        def make(B):
            ans = [None] * L
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(L), key = lambda i: A[i])
        oddnext1 = compute_greatest_elems(A)
        print B
        oddnext = make(B)
        B.sort(key = lambda i: -A[i])
        evennext2 = compute_smallest_elems(A)
        print B
        evennext = make(B)
        
        #print smallest_arr,greatest_arr
        
        odd = [False] * L
        even = [False] * L
        odd[L-1] = even[L-1] = True

        print oddnext,evennext
        print oddnext1,evennext2
        for i in xrange(L-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext1[i] is not None:
                even[i] = odd[evennext[i]]

        print odd,even
        return sum(odd)
