from collections import Ordereddict
class LRUCache:
    
    def __init__(self, capacity: int):
        self.LRU=OrderedDict()
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if key in self.LRU:
            self.LRU.move_to_end(key)
            return self.LRU[key] 

        return -1        

    def put(self, key: int, value: int) -> None:
        self.LRU[key]=value
        self.LRU.move_to_end(key)

        if (len(self.LRU)>self.capacity):
            self.LRU.popitem(last=False)
