# Runtime - 300 ms   Memory- 28 MB

class SegmentTreeNode(object):
    def __init__(self, start, end, sum_val=0):
        """
        :type nums: List[int]
        """
        self.start = start
        self.end = end
        self.sum = sum_val
        self.left = None
        self.right = None        
    
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        node,node_sum = self.buildTree(nums,0,len(nums)-1)
        self.root = node
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.update_helper(self.root,i,val)
        
    def update_helper(self,root, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """    
        if not root:
            return 0
        
        start = root.start
        end = root.end
        mid = start + (end-start)/2
        if start == end == i:
            temp = root.sum
            root.sum = val
            return val-temp
            
        if start <= i <= end:
            #print i,start,end
            left_val = self.update_helper(root.left,i,val)
            right_val = self.update_helper(root.right,i,val)
            upd_val = 0
            if left_val:
                upd_val = left_val
            if right_val:
                upd_val = right_val
            
            #print root.sum,upd_val
            root.sum = root.sum + upd_val
            return upd_val
        else:
            return 0
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_helper(self.root,i,j)
    
    def sum_helper(self,root,i,j):
        if not root:
            return 0
        
        start = root.start
        end = root.end 
        mid = (start + end) // 2
           
        if start == i and end == j:
            return root.sum
            
        if  j <= mid:
            return self.sum_helper(root.left,i,j)
        elif i >= mid+1:
            return self.sum_helper(root.right,i,j)
        else:
            #print i, mid
            left = self.sum_helper(root.left,i,mid)
            right = self.sum_helper(root.right,mid+1,j)
            return left+right
        
    def buildTree(self,nums,start,end):
        #print start,end
        
        N = len(nums)
        if N == 0:
            return None,0
        if N == 1:
            #print start,end,nums[0]
            new_node = SegmentTreeNode(start,end,nums[0])
            return new_node,nums[0]
        
        mid = start+(end-start)/2
    
        k = start
        
        left,left_sum = self.buildTree(nums[start-k:mid+1-k],start,mid)
        right,right_sum = self.buildTree(nums[mid+1-k:end+1-k],mid+1,end)
        
        node = SegmentTreeNode(start,end,left_sum + right_sum)
        node.left = left
        node.right = right
        
        return node,left_sum+right_sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
