"""

# list of movies that i loved

fav_movie=[]

while True:
    print("Movie no "+str(len(fav_movie)+1) +" or press ENTER to stop adding to the list.")
    movie =input()


    if movie == "":
        break


    fav_movie =fav_movie + [movie]


if len(fav_movie) != 0:
    print("The list are ")
    for i in range(len(fav_movie)):
        print(fav_movie[i])



#  The in and not in keyword

my_tech=['iphone','android','ASUS Laptop','monitor']

print('Enter a tech name: ')
name = input()
if name not in my_tech:
    print('Nope its not in the list')
else:
    print(name+ "is my tech")
    

# Assuming mutiple vules at once

chocolate_milk_shake = ['chocolate','milk','ice_cream','blender']
x,y,z,q = chocolate_milk_shake

print(x,y,z,q)

"""

# Strings are list too

a = 'WHATS A LIST NOW?'
print(a[0])

# strings are immutable  forms of list,that is they can not be changed ,while lists can be modified
