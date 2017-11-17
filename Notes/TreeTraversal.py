'''
Pre-Order: Current, left, right
In Order(Infix): left, center, current
Post Order: left, right, current
Breadth: Level by level, each from left to right



x = seq1()
z_iter = iter(x)
next(x_iter)


def seq1():
    yield 1
    yield 2
    for i in seq2(): #or can be simplified to yield from seq2()
        yield i

def seq2():
    yield 3
    yield 4

'''