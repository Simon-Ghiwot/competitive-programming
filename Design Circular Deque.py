class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0] * k
        self.capacity = k
        self.size = 0
        self.rear = -1
        self.front = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = ((self.front - 1) % self.capacity + self.capacity) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.deque[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear = -1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = ((self.rear - 1) % self.capacity + self.capacity) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear = -1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.capacity == self.size
