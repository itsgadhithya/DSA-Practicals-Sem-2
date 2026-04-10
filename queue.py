class Queue:
    def __init__(self):
        self.qu = []

    def enqueue(self, element):
        self.qu.append(element)

    def dequeue(self):
        return self.qu.pop(0)

    def peek(self):
        return self.qu[-1]


traffic_queue = Queue()
traffic_queue.enqueue("Element 1")
traffic_queue.enqueue("Element 2")
traffic_queue.enqueue("Element 3")
traffic_queue.enqueue("Element 4")

print(traffic_queue.qu)

print(traffic_queue.peek())

print(traffic_queue.dequeue())
print(traffic_queue.dequeue())

print(traffic_queue.qu)
