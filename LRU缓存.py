
from collections import OrderedDict
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.lruCache = OrderedDict()  # 内置一个 有序字典 或 将该类继承自 有序字典类 
        
    def get(self, key: int) -> int:
        
        if key in self.lruCache:
            self.lruCache.move_to_end(key)  # get到该值 放到最前
            return self.lruCache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.lruCache:
            self.lruCache.move_to_end(key)  # put到该值 放到最前
            
        self.lruCache[key] = value
            
        if len(self.lruCache) > self.capacity:
            self.lruCache.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
