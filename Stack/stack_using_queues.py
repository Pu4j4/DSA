#brute force (using two queues)
from collections import deque
class Stack:
    def __init(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self,x):
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top = self.q1.popleft()
        #swap
        self.q1, self.q2 = self.q2, self.q1
        return top
    def top(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top = self.q1.popleft()
        self.q2.append(top)
        self.q1, self,q2 = self.q2, self,q1
        return top
    def empty(self):
        return len(self.q1) == 0



#optimized
class Stack:
    def __init__(self):
        self.q = deque()

    def push(self,x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0