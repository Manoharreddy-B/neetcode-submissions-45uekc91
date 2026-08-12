class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}
        self.temp = []
        self.temp_set = set()
        
    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        
        if key in self.temp_set:
            self.temp_set.remove(key)
            self.temp.remove(key)
        self.temp_set.add(key)
        self.temp.append(key)
        return self.lru[key]

    def put(self, key: int, value: int) -> None:
        self.lru[key] = value
        if key in self.temp_set:
            self.temp_set.remove(key)
            self.temp.remove(key)
        self.temp.append(key)
        self.temp_set.add(key)

        if len(self.lru) > self.capacity:
            temp_to_delete = self.temp[0]
            self.temp_set.remove(temp_to_delete)
            del self.temp[0]
            self.lru.pop(temp_to_delete)













    # def get(self, key: int) -> int:
    #     if key not in self.lru:
    #         return -1

    #     # key was used, so move it to the most-recent position
    #     if key in self.temp_set:
    #         self.temp.remove(key)

    #     self.temp.append(key)
    #     self.temp_set.add(key)

    #     return self.lru[key]

    # def put(self, key: int, value: int) -> None:

    #     # If key already exists, remove its old position
    #     # because this put() makes it most recently used
    #     if key in self.lru:
    #         self.temp.remove(key)

    #     self.lru[key] = value
    #     self.temp.append(key)
    #     self.temp_set.add(key)

    #     # Evict only when we actually exceed capacity
    #     if len(self.lru) > self.capacity:
    #         temp_delete = self.temp[0]

    #         del self.temp[0]
    #         self.temp_set.remove(temp_delete)
    #         del self.lru[temp_delete]

