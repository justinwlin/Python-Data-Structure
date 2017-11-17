class MaxStack:
    def __init__(self):
        self.data = []
        self.maxNum = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        if self.maxNum is None or self.maxNum < val:
            self.maxNum = val
        tuple = (val, self.maxNum)
        self.data.append(tuple)

    def top(self):
        if (self.is_empty()):
            raise ("Stack is empty")
        return self.data[-1][0]

    def pop(self):
        if (self.is_empty()):
            raise ("Stack is empty")
        tuple = self.data[-1]
        self.data.pop()
        return tuple[0]

    def max(self):
        if (self.is_empty()):
            raise ("Stack is empty")
        tupleAccess = self.data[-1]
        return tupleAccess[1]
