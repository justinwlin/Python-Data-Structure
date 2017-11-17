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

def balanced(x):
    stack = ArrayStack()
    balanced = True
    index = 0
    while index < len(x) and balanced:
        symbol = x[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not match(top, symbol):
                    return False
        index = index + 1
    if balanced and stack.is_empty():
        return True
    else:
        return False

def match(opening, closing):
    opens = "([{"
    close = ")]}"
    return opens.index(opening) == close.index(closing)


x = "((()))"
y = "[[()]]]"
print(balanced(x))
print(balanced(y))
