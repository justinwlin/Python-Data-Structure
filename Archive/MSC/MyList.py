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

lst = MyList()
lst1 = [1,2]
lst2 = [2,3]
print(lst1 + lst2)
