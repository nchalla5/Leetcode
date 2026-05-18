import random

class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False

        self.set[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False

        idx = self.set[val]
        last_val = self.list[-1]
        self.list[idx] = last_val
        self.set[last_val] = idx
        self.list.pop()
        del self.set[val]

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()