'''

# static method
class MyClass(object):
    @staticmethod
    def the_static_method(x):
        print(x)

MyClass.the_static_method(2)
'''

'''
from datetime import date

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name, date.today().year - year)


    @staticmethod
    def isAdult(age):
        return age> 18


person1= Person('mayank',21)
person2 = Person.fromBirthYear('mayank',1996)

print (person1.age)
print (person2.age)

print (Person.isAdult(22))
'''


class Mathmatics:

    def addNumbers(x,y):
        return x+y

# create addNumbers static method
Mathmatics.addNumbers=staticmethod(Mathmatics.addNumbers)

sum = Mathmatics.addNumbers(5,10)

print(sum)
