# Python Mutiple heritance or Sub Class 
# pass
class Class1:
    def m(self):
        print('In Class1')

class Class2(Class1):
    pass

class Class3(Class1):
    def m(self):
        print('In Class3')

class Class4(Class2,Class3):
    pass


obj = Class1()
obj1= Class2()
obj2= Class3()
obj3= Class4()


obj.m()
obj1.m()
obj2.m()
obj3.m()
