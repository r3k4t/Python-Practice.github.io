'''
class Point2D:
    def __init__(self,x,y):
        self.x= x
        self.y = y

    # Repr is using for professional purposes(Example:Developer,Senior Software Engineer)
    def __repr__(self):
        return f'Point2D({self.x,self.y})'

    # str is using for general purposes
    def __str__(self):
        return f'Class:Point2D, '\
               f'x:{self.x}, y:{self.y}'


p1 = Point2D(1,2)
p2 = Point2D(2,3)



print(repr(p1))
print(str(p2))

'''


class Point2D:
    def __init__(object,x,y):
        object.x = x
        object.y = y

    # Repr is using for professional purposes(Example:Developer,Senior Software Engineer etc)
    def __repr__(object):
       return f'Point2D:({object.x},{object.y})'

   # str is using for general purposes
    def __str__(object):
       return f'Class:Point2D, '\
              f'x:{object.x},y:{object.y}'

p1 = Point2D(1,2)
p2 = Point2D(2,3)

print(repr(p1))
print(str(p1))
