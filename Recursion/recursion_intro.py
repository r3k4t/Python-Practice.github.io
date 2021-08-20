#A function to calculate the factorial of a number
#4! = 4X3X2X1 ///\ 4 X 3!
#3! = 3x2x1
#5! = 5x4x3x2x1
#5! = 5 x 4 x 3 x 2 x 1!

'''
# looping
def factorial(n):
    temp = 1
    for i in range(2,n+1):
        temp = temp*i  
    return temp
print(factorial(int(num)))


# recursion
def factorial2(n):
    if n ==  1:
        return 1
    return n*factorial2(n-1)
 
 
num = input()

print(factorial(int(num)))
print(factorial2(int(num)))


'''

#Using builtin function math

import math 
num = input()
var=math.factorial
print(var(int(num)))



