import random

class RandomizedSet:

    def __init__(self):
        self.numbers = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.numbers.append(val)
        self.dict[val] = len(self.numbers) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # 마지막 요소 <-> val 순서 바꾸고 pop하기
        last_val = self.numbers[-1]
        curr_idx = self.dict[val]
        self.numbers[curr_idx] = last_val
        self.dict[last_val] = curr_idx
        
        self.numbers.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.numbers)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()