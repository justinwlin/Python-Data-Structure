class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()

class Queue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.inbox = ArrayStack()
        self.outbox = ArrayStack()
        self.sizeOfStack = 0

    def __len__(self):
        return len(self.inbox)

    def is_empty(self):
        return self.sizeOfStack

    def enqueue(self, elem):
            self.inbox.push(elem)
            self.sizeOfStack += 1

    def dequeue(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty(): #O(n)
                self.outbox.push(self.inbox.pop())
                self.sizeOfStack -= 1
            return self.outbox.pop()
        else:
            return self.outbox.pop()

    def first(self):
        if self.inbox.is_empty() and (not self.outbox.is_empty()):
            return self.outbox.data[len(self.outbox.data) - 1]
        if not self.inbox.is_empty():
            return self.inbox.data[0]
