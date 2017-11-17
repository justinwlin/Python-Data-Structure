def fibonacci(n):
    # lst = []
    # for i in range(0,n):
    #     if i < 2:
    #         lst.append(i)
    #         yield i
    #     else:
    #         first = lst[i - 1]
    #         second = lst[i - 2]
    #         lst.append(first + second)
    #         yield first + second

    a, b = 0, 1 #setting a = 0 , b = 1
    while True: #keeps it repeating when yield is called again
        yield a
        a, b = b, a + b #a = old b; b = a + b, so that it advances it more.


g = fibonacci(10)
for i in range(0,10):
    print(next(g))


