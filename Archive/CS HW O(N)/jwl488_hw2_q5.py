def split_parity(lst):
    switch1 = 0
    switch2 = 0
    for i in lst: #O(n)
        if i % 2 == 1: #if odd...
            lst[switch1], lst[switch2] = lst[switch2], lst[switch1]
            switch1 = switch1 + 1
            switch2 = switch2 + 1
        if i % 2 == 0: #if even
            switch2 = switch2 + 1
    return lst


'''
    
    [1,2,3,4,5]
    check 0th index... 
    
    If it is odd... Increase both index...
    switch1 & 2 = 1
    
    If it is even... switch 2 ++...
    if it is odd...
        switch 1 and 2...
'''

input = [3,9,6,4,6,12,13]
print("Original Input:" + str(input))
print("Final Output:" + str(split_parity(input)))