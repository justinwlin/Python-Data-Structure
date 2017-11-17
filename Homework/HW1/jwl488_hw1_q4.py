def multipleTen():
    return [10 ** k for k in range (0,6)]


def pronics():
    return [n * (n + 1) for n in range(0,10)]


def alphabet():
    return [chr(k) for k in range(97, 123)]


print(multipleTen())
print(pronics())
print(alphabet())