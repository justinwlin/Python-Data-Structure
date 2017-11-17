# def remove_all(lst, value):
#     empty = []
#     try:
#         for x in lst:
#             if x!= value:
#                 empty.append(x)
#         if len(empty) == len(lst):
#             raise ValueError
#     except ValueError:
#         return ValueError


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

#
# print(remove_all([4,4,4], 4))
