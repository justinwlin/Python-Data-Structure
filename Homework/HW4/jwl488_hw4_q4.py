def find_duplicates(lst):
    result = []
    for i in lst:
        index = abs(i) - 1
        if(lst[index] < 0):
            result.append(abs(i))
        else:
            lst[index] = lst[index] * -1
    return result


# print(find_duplicates([1, 3, 1, 2, 5, 2, 3, 4, 5, 6]))