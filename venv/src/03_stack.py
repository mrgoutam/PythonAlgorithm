class Stack:
    def __init__(self):
        self.stack = []

    def peak(self):
        return self.stack[-1]

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.remove(self.peak())

    def traverse(self):
        index = len(self.stack)-1
        while index>=0:
            print(self.stack[index])
            index -= 1


stack = Stack()
stack.push(6)
stack.push(9)
stack.push(4)
stack.push(10)

print('----traverse-----')
stack.traverse()

print('----Peak-----')
print(stack.peak())

print('----Pop-----')
stack.pop()
stack.traverse()

print('----Push 50-----')
stack.push(50)
stack.traverse()
