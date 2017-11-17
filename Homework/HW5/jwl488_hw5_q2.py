class Dequeue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * Dequeue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (self.size == 0)

    def first(self):
        if self.is_empty():
            raise ('Queue is empty')
        return self.data[self.front]

    def last(self):
        back = (self.front + self.size - 1) % len(self.data)
        return self.data[back]

    def add_first(self, item):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front - 1) % len(self.data)
        self.data[avail] = item
        self.front = (self.front - 1) % len(self.data)
        self.size += 1

    def add_last(self, item):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data [avail] = item
        self.size += 1

    def delete_first(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        if(self.size < len(self.data) // 4):
            self.resize(len(self.data) // 2)
            self.data[self.front] = None
            self.size -= 1
        return value

    def delete_last(self):
        back_ind = ((self.front + self.size) % len(self.data)) - 1
        value = self.data[back_ind]
        self.data[back_ind] = None
        self.size -= 1
        return value

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front
        for new_ind in range(self.size):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front = 0

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
            raise ("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise ("Stack is empty")
        return self.data.pop()


class MidStack:
    def __init__(self):
        self.arrStack = ArrayStack()
        self.arrD = Dequeue()
        self.size = 0


    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self.size

    def push(self, e):
        self.arrD.add_last(e)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise ('It is empty')
        return self.arrD.last()

    def pop(self):
        self.size -= 1
        return self.arrD.delete_last()

    def mid_push(self, elem):
        counter = self.size // 2
        counterTogether = 0
        while counterTogether < counter:
            self.arrStack.push(self.arrD.delete_last())
            counterTogether += 1
        self.arrD.add_last(elem)
        while not self.arrStack.is_empty():
            self.arrD.add_last(self.arrStack.pop())
            self.size += 1
        # if(self.size % 2 == 0):
        #     self.stack.push(elem)
        # else:
        #     self.arrD.add_first(elem)
        # self.size += 1


        # midIndex = (self.arrD.first + self.arrD.last) // 2
        # while self.size > midIndex:
        #         self.arrStack.push(self.arrD.delete_last())
        #         self.size -= 1
        # self.arrD.add_last(elem)
        # while not self.arrStack.is_empty():
        #     self.arrD.add_last(self.arrStack.pop())
        #     self.size += 1

# midS = MidStack()
# midS.push(2)
# midS.push(2)
# midS.push(2)
# midS.push(2)
# midS.push(2)
# midS.mid_push(10)
# print(midS.top())
# midS.pop()
# print(midS.top())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
#
# print(midS.arrD.data)
# print(midS.arrStack.data)


