"""
# making  a list
a = [1, 2, 3]
b = ['a','b','c']
z = [3.1415,'pi',23]

print(b)

print(z)

# Nested lists

x = [[1,2,3],[4,5,6]]
print(x[1][1])

# Negetive index

p = [1,2,3,4]
print(p[-1])
print(p[-2])

# sub lists & slicing

q = [1,2,3,4,5,6]
print(q[0:5])
# q[start_index:end_index+1]
# q[0:4+1]
# print(q[1:4])
print(q[0:-2])
print(q[1:-1])

# q[start_index:end_index+1]
# q[0:-3+1] = q[0:-2]

# print(q[:4])
# print(q[0:])
print(q[:])

a = [1,2,3,4]
b = ['x','y','z']
ab = a + b
print(ab)

new_x = x*2
print(new_x)

"""

p= ['a',0,9]
del p[0]
print(p)


