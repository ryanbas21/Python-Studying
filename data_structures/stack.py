class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
       return self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def view(self):
        if len(self.stack) == 0:
            return 'Stack is empty'

        return self.stack[-1]

    def size(self):
        return len(self.stack)
    def isEmpty(self):

        return len(self.stack) == 0


def revString(str):
    x = Stack()
    newStr = ''

    for letter in str:
        x.push(letter)

    while x.size() != 0:
        newStr += x.pop()

    return newStr
