from circular_queue import CircularQueue

qu = CircularQueue(4)

print(qu.isEmpty())
print(qu.isFull())

print(qu.q)

qu.enqueue(20)
qu.enqueue(20)
qu.enqueue(20)
qu.enqueue(20)

print(qu.q)

qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()

print(qu.isEmpty())
print(qu.isFull())


print(qu.q)

print(qu.isEmpty())
print(qu.isFull())
