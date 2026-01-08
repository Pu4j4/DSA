class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
        print(f"pushed {x}")
    def pop(self):
        if self.is_empty():
            print("stack is empty, cannot pop")
            return None
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            print("stack is empty,nothing to peek")
            return None
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0