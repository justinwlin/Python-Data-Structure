class Vector:
    def __init__(self, d):
        if isinstance(d, list):
            self.coords = d
        else:
            self.coords = [0] * d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
            result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
            return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)

    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result

    def __mul__(self, n):
        if isinstance(n, Vector):
            if (len(self) != len(n)):
                raise ValueError("dimensions must agree")
            result = 0
            for j in range(len(self)):
                result += self[j] * n[j]
            return result
        else:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * n
            return result


    def __rmul__(self, n):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * n
        return result




u = Vector([2,2,2])
v = Vector([1,1,1])

print(u * v)
print(-v)
print(3 * v)
