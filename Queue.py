#Queue
from collections import deque

q = deque()
q.appendleft(5)
q.appendleft(9)
print(q)
q.pop() #--> returns 5
print(q)

#Could be implemented just using array
# list = []
# list.insert(0, 3)
# list.insert(0, 4)
# but this shift all other elements to the right

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)



