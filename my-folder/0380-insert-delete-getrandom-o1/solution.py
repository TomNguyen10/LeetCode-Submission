class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hash_map = {}

    def insert(self, val: int) -> bool:
        if val not in self.hash_map:
            self.arr.append(val)
            self.hash_map[val] = len(self.arr) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            location = self.hash_map[val]
            if location < len(self.arr) - 1:
                last = self.arr[-1]
                self.hash_map[last], self.arr[location] = location, last
            self.arr.pop()
            self.hash_map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        loc = random.randint(0, len(self.arr) - 1)
        return self.arr[loc]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
