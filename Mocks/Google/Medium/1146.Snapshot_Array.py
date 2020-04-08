import collections

class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.curr_arr = [0]*length
        self.changed_vals = collections.defaultdict(list)
        self.snap_arr = collections.defaultdict(dict)
        self.snap_count = 0
        
    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.curr_arr[index] = val
        self.changed_vals[index]=val

    def snap(self):
        """
        :rtype: int
        """
        self.snap_arr[self.snap_count] = self.changed_vals.copy()
        self.snap_count += 1 
        return self.snap_count-1
        
    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        if index in self.snap_arr[snap_id]:
            return self.snap_arr[snap_id][index]
        else:
            return 0
    

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
