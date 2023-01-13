class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.values = {}

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.values[num] = self.values.get(num, 0) + 1
        if len(self.queue) > self.k:
            poped = self.queue.popleft()
            self.values[poped] -= 1
            if self.values[poped] == 0:
                self.values.pop(poped)
        if len(self.values) > 1 or len(self.queue) < self.k or self.value not in self.values:
            return False
        return True


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
