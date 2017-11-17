from .Arraystack import ArrayStack

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:40:56 2017

@author: selina
"""

a = ArrayStack()
a.push("test")
print(a.pop())
print(a.data)
x = 1
print(x.data)

# def print_in_reverse(s):
#     chars_stack=ArrayStack.ArrayStack()
#
#     for chars in s:
#         chars_stack.push(chars)
#     while not chars_stack.is_empty():
#         ch = chars_stack.pop()
#         print(ch,end="")
#     print("")
#
# def eval_postfix_exp(exp_str):
#     operators="+-*/"
#     exp_lst = exp_str.split()
#     S=ArrayStack.ArrayStack()
#     for token in exp_lst:
#         if(token not in operators):
#             S.push(int(token))
#         else:
#             arg2=S.pop()
#             arg1=S.pop()
#         if(token=='+'):
#             res =arg1+arg2
#         elif(token=='-'):
#             res=arg1-arg2
#         elif(token=='*'):
#             res=arg1*arg2
#         else:
#             res=arg1/arg2
#
#         S.push(res)
#     return(S.pop())