class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}
        self.temp = []
        
    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        
        if key in self.lru:
            self.temp.remove(key)
            
        self.temp.append(key)
        return self.lru[key]

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.pop(key)
            self.temp.remove(key)
        self.temp.append(key)
        self.lru[key] = value

        if len(self.lru) > self.capacity:
            temp_to_delete = self.temp[0]
            del self.temp[0]
            self.lru.pop(temp_to_delete)
