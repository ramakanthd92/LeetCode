# Runtime -     Memory -

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = set() 

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hash_set:
            self.hash_set.add(val)
            return True
        return False
    

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hash_set:
            self.hash_set.remove(val)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.hash_set) > 0:
            val = self.hash_set.pop()
            self.hash_set.add(val)
            return val
        return None
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
