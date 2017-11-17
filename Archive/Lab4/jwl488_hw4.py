def split_by_sign(lst, low, high, empty = None):
    if empty == None:
        lst[low:high]
        low = 0
        high = len(lst) - 1
    if len(lst) == 1:
        return lst[0:1]
    if low < high:
        if lst[0] < 0:
            return split_by_sign(lst[1:], low, high, 1) + lst[0:1]
        if lst[0] > 0:
            return split_by_sign(lst[0:1], 0, 0, 1) + split_by_sign(lst[1:], low, high, 1)
    return lst


def permutation(lst, low, high, empty = True):
    if empty:
        lst[low:high]
        empty = False
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for j in permutation(xs, low, high, empty):
                l.append([x] + j)
        return l


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


def find_duplicates(lst):
    result = []
    for i in lst:
        index = abs(i) - 1
        if(lst[index] < 0):
            result.append(abs(i))
        else:
            lst[index] = lst[index] * -1
    return result


def remove_all(lst, value):
    try:
        initialLen = len(lst)
        low = 0
        high = len(lst) - 1
        while lst[high] == value: #o(n) if everything is, but otherwise o(1)
            lst.pop()
            if low <= high:
                high -= 1
            if high < 0:
                return lst
        for x in range(0, len(lst) -1): #o(n) Worst case
            if low == high:
                break;
            if lst[low] == value:
                    while lst[high] == value:
                        lst.pop()
                        high -= 1
                    if lst[high] != value:
                        lst[high], lst[low] = lst[low], lst[high]
                        lst.pop()
                        high -= 1
                        while lst[high] == value:
                            lst.pop()
                            high -= 1
            else:
                low += 1
        if len(lst) == initialLen:
            raise ValueError
        return lst
    except ValueError:
        return "There was no value in the list"