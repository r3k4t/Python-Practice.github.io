
# Multiple quote = """ hi """


"""# use of infinite loop with break statement

while True:
    print("Please Enter your Name!")
    name = input()
    if name == "your name":
           break

print('Thank You')

# use of continue statement

while True:
    print("Who are you")
    name = input()
    if name != "Cybersecurity Specialist":
        continue
    print("hello there  "+name+"  What is the passcode?")
    password=input()
    if password == "kasse Biryani":
        break
print ("eaam eaam eaam.Finish")

# Series - 1+2+3+4

sum=0
for i in range(1,5):
     sum=sum+i
print (sum)

# Series - 1+2^2+3^2+4^2

sum=0
for i in range(1,5):
    sum=sum+i*i
print (sum)

# Series - 1+3+5+7+9

obb_sum=0
for i in range(1,10,2):
    obb_sum=obb_sum+i
print(obb_sum)

# Series - 2+4+6+8

even_sum=0
for i in range(2,10,2):
    even_sum=even_sum+i
print(even_sum) """

# Series - 1+(1+2)+(1+2+3)+(1+2+3+4)

sum=0
for i in range(1,5):
    for j in range(i,sum+i):
        sum=sum+i
print(sum)


