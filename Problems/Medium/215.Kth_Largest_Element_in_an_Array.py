# Runtime - 96 ms  Memory - 13.8 MB

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        N = len(nums)
        
        def random_elem(st,en):
            return random.randint(st,en)
        
        def swap(l,r):
            nums[l],nums[r] = nums[r],nums[l]
            
        def partition(pivot,st,en):
            l = st
            r = st
            pivot_elem = nums[pivot]
            swap(pivot,en)
            while (l < en and r < en):
                if nums[r] < pivot_elem:
                    swap(l,r)
                    l += 1
                r += 1 
            swap(en,l)
           # print nums,l
            return l
            
            
        def select(l,r):
            if l == r:
                return nums[l]
            pivot = random_elem(l,r)
           
            pivot = partition(pivot,l,r)
           # print l,r
            
            if pivot == N-k:
                return nums[pivot]
            elif pivot > N-k:
                return select(l,pivot-1)
            elif pivot < N-k:
                return select(pivot+1,r)
            
        return select(0,len(nums)-1)
               
