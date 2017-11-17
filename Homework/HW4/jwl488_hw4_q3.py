import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size


    def extend(self, other):
        for elem in other:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if ind < 0:
            ind += len(self)
        return self.data[ind]


    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        self.data[ind] = val

    def __str__(self):
        empty = "["
        for i in self:
            if i != None:
                empty += str(i)
                empty += ", "
        empty = empty[0:len(empty)-2]
        empty += "]"
        return empty

    def __repr__(self):
        print(self)

    def __add__(self, other):
        lst = []
        lst.extend(self)
        lst.extend(other)

    def __iadd__(self, other):
        for i in other:
            self.append(i)

    def insert(self, index, val):
        try:
            if index < 0 or index > len(self) + 1:
                raise IndexError
            empty = []
            counter = 0
            if index == 0:
                empty.append(val)
                for firstloop in self:
                    empty.append(firstloop)
            if index > 0:
                for secondloop in self:
                    empty.append(secondloop)
                    counter += 1
                    if counter == index:
                        empty.append(val)
            empty.resize(empty, len(empty) * 2)
            return empty
        except IndexError:
            return IndexError

    def pop(self):
        lastIndex = len(self) - 1
        while self[lastIndex] == None:
            lastIndex -= 1
        if lastIndex < len(self) //4:
            self.resize(self, len(self) - 2)
        temp = self[lastIndex]
        self[lastIndex] = None
        return temp



mlst = MyList()
for i in range(1, 4+1):
    mlst.append(i)

print(mlst.insert(-1,3))
print(mlst.pop())
print(mlst.pop())
print(mlst.pop())
print(mlst)
