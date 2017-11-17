import sys
'''
[<term (var)> for <var> in <interable-collections]
[<term(var)> for <var> in <iterable collections> if (cond (var)>)]
    ex. of conditional list 
    res_lst[]
    for <var> in interable_collections>:
        if(<cond(var)>):
            res_lst.append(<term(var)>)
    return res_lst

'''
#=======================
# Creating a function within a list...
#=======================
def squares_list(n):
    return [k*k for k in range(1,  n + 1)]

def tens_list(n):
    return [10 * k for k in range (1, n + 1)]

def ascii_value(s):
    return [ ord (ch) for ch in s]

#=======================
# Creating a list with a condition within the list when returning it
#=======================

def factors(num):
    return [num//k for k in range(1, num // 2 + 1) if num % k == 0]

def shallowcopy(lst):
    return [item for item in lst]
'''
This is a shallow copy b/c when you return each item in the list, it references
the actual original item. Thereby if you modify any of the items in this, when you return it etc. 
it will affect the original. 
'''

#=======================
# MAIN ENTRY POINT
#=======================

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print(squares_list(10))
    print(factors(100))

if __name__ == "__main__":
    main()
