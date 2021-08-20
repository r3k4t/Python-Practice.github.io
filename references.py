"""

a = [1,2,3]
b = a

b[1] = 3.1416

print(a)


def f(some_list):
    some_list.append('ok')

x =[1,2,3]

f(x)

print(x)

"""

import copy as cp

def f(some_list):
    some_list.append('ok')


x=[1,2,3]
s=cp.copy(x) # a copy of the list is made

f(s)

print(x)

