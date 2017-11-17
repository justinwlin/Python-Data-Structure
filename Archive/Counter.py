import sys

'''
Notes:
========
Classes
========
This is on how to create classes.
Everytime you instantiate a class, it doesn't affect each other.
it is separate from each other.

lst = [counter()] * 3
- This is just creating a list * 3; but all three boxes are pointing to the same reference/same object

lst2 = [Counter() for i in range(3)]
- Everytime there is an i, you call Counter(), which creates three separate object in total
or one time everytime it is called

======================
Definitions MSC Notes
======================
Iterable: an object that produces an iterator by calling the iter(...) function



for <var> in <iterable>
lst [ 1, 2, 3 ]
s = "abc"
r = range(3) 
(All the above are examples of iterable objects); but you can also do...

lst_iterator = ier(lst)
s_iterator = iter(s)
r_iterator = iter(r)

======SKIP TO THE CODE TO ITERATOR SECTION==========

'''

class Counter:
    def __init__(self,val = 1):
        self.val = val

    def print_and_inc(self):
        print(self.val)
        self.val += 1

'''
===================
Notes on Iterators
===================
>>> type(l)
    <class 'list'>
>>> type (s_iter)
    <class 'str_iterator'>

Question becomes, what are iterators?
- Iterators: an object that allows a collection of values by subsequent 
calls to the next(...) function; (A stopIteration exception is thrown when there are no
more elements left.)
=====================
'''
#======================
#ITERATION EXAMPLE NOTES
#=======================
def interation():
    l = [1, 2, 3]
    s = "abc"
    r = range(3)

    l_inter = iter(l)
    s_iter = iter(s)
    r_iter = iter(r)

'''
=========================
Console Command Examples
=========================
type(l_inter)
type(s_iter)
type(r_iter)

next(l_inter) <-- will begin to increment through l, will return: 1, 2, 3... error
next(l_inter)
next(l_inter)

next(s_iter) <-- will iterate through s, will: a, b, c
next(r_iter)
==========================
'''

'''
======================
Why you use iteration
======================

r = range(3)
r_iteration = iter(r)
try:
while(end == false)
    curr = next(r_iterator)
    print(curr)
except stopIteration:
    end = True

- Basically this is a lower-level implementation when we use soething like:
for curr in range(3)
    print(curr)
    
======================
ITERATOR EXAMPLE
=====================
l = [1,2,3,4]
l_terator = iter(l)

next(l_terator)

etc etc. will start to iterate thro till hits an error. 

'''

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    c1 = Counter(1)
    c1.print_and_inc()
    c1.print_and_inc()

    interation()

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.




if __name__ == "__main__":
    main()
