class Queue:
    def __init__(self):
        self.qu = []

    def enqueue(self, element):
        self.qu.append(element)

    def dequeue(self):
        return self.qu.pop(0)

    def peek(self):
        return self.qu[-1]
