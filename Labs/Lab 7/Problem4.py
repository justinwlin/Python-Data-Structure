class Deque:
    def __init__(self):
        self.data = []
        self.num_of_elems = 0
        self.last_index = len(self.data) - 1

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def first(self):
        return self.data[0]

    def last(self):
        return self.data[self.last_index]

    def add_first(self, elem):
        self.data.insert(0, elem)

    def add_last(self, elem):
        self.data.append(elem)

    def delete_first(self):
        first = self.data[0]
        self.data = self.data[1:]
        return first

    def delete_last(self):
        return self.data.pop()

a = Deque()
a.add_last(3)
print(a.data)
a.add_first(4)
print(a.data)
a.add_first(5)
print(a.data)
a.delete_first()
print(a.data)
a.delete_last()
print(a.data)