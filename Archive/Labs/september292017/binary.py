def binary(lst, val, low, high):
    mid = (low + high) // 2
    if low > high:
        return "none"
    else:
        if val < lst[mid]:
            return binary(lst, val, low + 1, high)
        elif val > lst[mid]:
            return binary(lst, val, low,high - 1)
        else:
            return mid

a = [1,2,3,4,5,6,7,8]
print(binary(a, 7, 0, 6))


