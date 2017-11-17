def factors(num):
    rangeNum = int (num ** 0.5) + 1
    lst = []
    #Difference between num ** 1/2 and num ** .5
    for i in range(1, rangeNum): #o(sqrt(n))
        if num % i == 0:
            lst.append(i)
            yield i
            j = len(lst) - 1
    for k in range(0, len(lst) - 1): #< o(sqrt(n))
        j = j - 1
        yield num // lst[j]

for curr in factors(100):
    print (curr)
