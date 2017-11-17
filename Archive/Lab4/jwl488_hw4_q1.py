'''
[-1, -2, -3, 1, 2, 3, -4]

1) Check the low index, if it is greater than 0, insert in the front
2) If it is less than 0, append to the end

3) Splice the list, so that it takes the first index, and the rest of the index.
a) Base case should return that number.
'''

def split_by_sign(lst, low, high, empty = None):
    if empty == None:
        lst[low:high]
        low = 0
        high = len(lst) - 1
    if len(lst) == 1:
        return lst[0:1]
    if low < high:
        if lst[0] < 0:
            return split_by_sign(lst[1:], low, high, 1) + lst[0:1]
        if lst[0] > 0:
            return split_by_sign(lst[0:1], 0, 0, 1) + split_by_sign(lst[1:], low, high, 1)
    return lst

    # if empty == None:
    #     lst[low:high]
    #     low = 0
    #     high = len(lst) - 1
    # if low < high:
    #     if lst[low] < 0:
    #         temp = lst[low]
    #         lst.pop(low)
    #         lst.append(temp)
    # return lst

# a = [-1, -2, -3, 1, 2, 3, -1, -2]
# print(split_by_sign(a, 0, 5))