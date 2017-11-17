'''
====================================
THREE VARIABLE RANGE NOTES
====================================
for i in range(4, 10, 2):
...     print(i)
4
6
8

IMPLEMENTATION TO THIS CAN BE DONE:

def my_range(start, stop, step)
    curr = start
    while(curr < stop)
        yield curr
        curr += step
====================================
END OF THREE VARIABLE RANGE NOTES
====================================


====================================
GENERAL NOTES
====================================


====================================
END OF GENERAL NOTES
====================================

'''

def f():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

'''
=======================================================
NOTES ON DEF F(): IF YOU WERE TO RUN A CONSOLE COMMAND
=======================================================
>> type(f)
    <class 'function'>

>> g = f()

>> type(g)
    <class 'generator'>

>> g
    <generator object f at #some address number>
    
>> next (g)
    1
>> next (g)
    2
>> next (g)
    3
>>next (g)
    ERROR
==============================
END OF NOTES ON DEF(F):
==============================
    
=============================
WHAT IS YIELD VERSUS RETURN?
=============================
It is like return, in that it breaks the function and comes back out with a value. 

However, when the Yield exits the function, it stores the current states of the function on the side,
and when you call next(g) it continues from where it was left off. 

So this is helpful, b/c it differs from return that would just terminate and start over if called again, compared
to yield to where it just starts to where it was left off. 


You can also use this generator so in the future, you can use it in the future. 
===============================
END OF WHAT IS YIELD
===============================
'''

#Implementing a range function
def my_range(start, stop, step):
    curr  = start
    while(curr < stop):
        yield curr
        curr += step

'''
r = my_range(1,10,2)
print(next(r))
print(next(r))
print(next(r))

===========================================
WHY AN IMPLEMENTATION LIKE THIS DIFFERS
============================================

A LST would for ex. if u createa  million number list, it would take a lost of memory and makes it up front. 

Compared to iterating with a yield, there is only really 4 variable, and only iterates through what is necessary, and doesn't
store the entire range upfront. Rather it returns it when necessarily. 
'''

#Implement Factors using Yield

def factors(num):
    for curr in range(1, num + 1):
        if(num % curr == 0):
            yield curr

'''
========================================================
MORE NOTES ON YIELD AND SIMILAR TYPES OF IMPLEMENTATION
========================================================

This type of implementation is called a lazy function
Allows to produce an implicit sequence
1) Doesn't store all of the elements inside the memory at once
2) Doesn't evaluate or compute all the elements upfront

'''