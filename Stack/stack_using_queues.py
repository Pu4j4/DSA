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

