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