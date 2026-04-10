class CircularQueue:
    def __init__(self, max):
        self.MAX = max
        self.head = 0
        self.tail = 0
        self.q = [None] * self.MAX
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.MAX

    def enqueue(self, item):
        if self.isFull():
            raise IndexError("The given queue is full!")
        self.q[self.tail] = item
        self.tail = (self.tail + 1) % self.MAX
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("The given queue is empty!")
        self.front = (self.front + 1) % self.MAX
        self.size -= 1


qu = CircularQueue(4)

print(qu.isEmpty())
print(qu.isFull())

print(qu.q)

qu.enqueue(20)
qu.enqueue(20)
qu.enqueue(20)
qu.enqueue(20)

print(qu.q)

print(qu.isEmpty())
print(qu.isFull())
