class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            self.d.move_to_end(key, last=False)
            return self.d[key]

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        self.d.move_to_end(key, last=False)
        while len(self.d) > self.capacity:
            self.d.popitem(last=True)       


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)