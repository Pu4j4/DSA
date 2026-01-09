class Stack:
    def __init__(self):
        self.stack = []
    def my_stack(self):
        self.stack.append(10)
        self.stack.append(20)
        self.stack.append(30)

        print("top element:", self.stack[-1])
        print("popped Element:",self.stack.pop())
        print("top element after popping:", self.stack[-1])
        print("stack size:",len(self.stack))
        print("is stack empty:",len(self.stack)==0)

s = Stack()
s.my_stack()