def sumSquares(n):
    n -= 1
    hold = 0
    while n > 0:
        hold += n * n
        n -= 1
    return hold


def sumSquare2(n):
    return sum([k * k for k in range(0, n)])


def sumSquareOdd(n):
    n -= 1
    hold = 0
    while n > 0:
        if n %2 == 1:
            hold += n * n
            n -= 1
        n -= 1
    return hold


def sumSquareOddShort(n):
    return sum(k *k for k in range(0, n) if k % 2 == 1)


'''
print(sumSquares(4))
print(sumSquare2(4))
print(sumSquareOdd(4))
print(sumSquareOddShort(4))
'''
