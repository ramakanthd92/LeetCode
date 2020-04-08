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
        node,node_sum = self.buildTree(nums,0,len(nums))
        self.root = node
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
    
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
            return val-root.sum
            
        if start < i < end:
            
        
        if end < i:
            return self.update_helper(root.right,i,val)
        elif start > i:
            return self.update_helper(root.left,i,val)
        else:
            return self.sum_helper(root.left,i,mid) + self.sum_helper(root.right,mid+1,j)
    
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
        mid = start + (end-start)/2
        
        if start == i and end == j:
            return root.sum
        
        if end < i:
            return self.sum_helper(root.right)
        elif start > j:
            return self.sum_helper(root.left)
        else:
            return self.sum_helper(root.left,i,mid) + self.sum_helper(root.right,mid+1,j)
    
    def buildTree(self,nums,start,end):
        N = len(nums)
        if N == 0:
            return None,0
        if N == 1:
            new_node = SegmentTreeNode(start,end,nums[0])
            return new_node,nums[0]
        start = 0
        end = N-1
        mid = start+(end-start)/2
        
        left,left_sum = self.buildTree(nums[start:mid+1],start,mid)
        right,right_sum = self.buildTree(nums[mid+1:end+1],mid+1,end)
        
        node = SegmentTreeNode(start,end,left_sum + right_sum)
        node.left = left
        node.right = right
        
        return node,left_sum+right_sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
