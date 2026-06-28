class TimeMap:

    def __init__(self):
        self._dict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._dict:
            self._dict[key] = ([value], [timestamp])
        else: 
            self._dict[key][0].append(value)
            self._dict[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # find index of timestamp then access the value at that index
        if key not in self._dict:
            return ""
            
        intr_tuple = self._dict[key]
        val_tup = intr_tuple[0]
        time_tup = intr_tuple[1]
        index = self.binSearch(time_tup, 0, len(time_tup)-1, timestamp)

        if index is None:
            return ""
        return val_tup[index]

    def binSearch(self, time_tup, left, right, timestamp):
        if left > right:
            return left - 1 if left - 1>=0 else None

        mid = (left + right) //2
        if time_tup[mid] == timestamp:
            return mid
        elif time_tup[mid] > timestamp:
            right = mid - 1
            return self.binSearch(time_tup, left, right,timestamp)
        else: 
            left = mid + 1
            return self.binSearch(time_tup, left, right, timestamp)
        