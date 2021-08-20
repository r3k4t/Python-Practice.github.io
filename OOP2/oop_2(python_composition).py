class Component:

    # composite class constructor

    def __init__(self):
        print("Component Class object created...")


    # cpmposite class instance method

    def m1(self):
        print("Component class m1() method executed...")


class Composite:
    # composite class constructor
    def __init__(self):
        self.obj1 = Component()


        print("Composite class object also created...")

    # composite class instance method

    def m2(self):

        print("Composite class m2() method executed...")

# calling m1() method of component class
obj2 = Composite()

obj2.m2()
