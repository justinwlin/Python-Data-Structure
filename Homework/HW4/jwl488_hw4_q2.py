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


x = [1,2,3]
print(permutation(x, 0, 2))