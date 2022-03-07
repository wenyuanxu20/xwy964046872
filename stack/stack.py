class Stack():
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:

            return self.stack[-1]

        else:
            return None


stack = Stack()

stack.push(1)
stack.push(1)
stack.push(0)

print(stack.pop())

print(stack.get_top())