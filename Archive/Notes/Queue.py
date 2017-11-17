class ArrayQueue:
    INIT_CAP = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INIT_CAP
        self.front = 0
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, elem):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = elem
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is Empty')
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        if self.size < len(self.data)//4:
            self.__resize(len(self.data)//2)
        return answer

    def __resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0