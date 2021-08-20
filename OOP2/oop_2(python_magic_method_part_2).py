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

    def __add__(object,other):
        if isinstance(object,other.__class__):
           return Point2D(object.x+other.x,object.y+other.y)
        else:
           return None

    #substract
    def __sub__(object,other):
        if isinstance(object,other.__class__):
           return Point2D(object.x-other.x,object.y-other.y)
        else:
           return None

    #equal method
    def  __eq__(self,other):
        pass



p1 = Point2D(1,2)
p2 = Point2D(2,3)


p3 = p1 + p2
p4 = p1-p2

print(p3)
print(p4)
'''

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
    # add method
    def __add__(object,other):
        if isinstance(object,other.__class__):
           return Point2D(object.x+other.x,object.y+other.y)
        else:
           return None

    #substract method
    def __sub__(object,other):
        if isinstance(object,other.__class__):
           return Point2D(object.x-other.x,object.y-other.y)
        else:
           return None

    #equal method
    def  __eq__(object,other):
        if isinstance(object,other.__class__):
            return object.x == other.x and object.y == other.y



p1 = Point2D(1,2)
p2 = Point2D(2,3)
p6 = Point2D(1,2)


print(p1 == p6)
print(p1 is p6)
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
    # add method => __add__
    def __add__(object,other):
        if isinstance(object,other.__class__):
           return Point2D(object.x+other.x,object.y+other.y)
        else:
           return None

    #substract method==>__sub__
    def __sub__(object,other):
        if isinstance(object,other.__class__):
           return Point2D(object.x-other.x,object.y-other.y)
        else:
           return None

    #equal method =>__eq__
    def  __eq__(object,other):
        if isinstance(object,other.__class__):
            return object.x == other.x and object.y == other.y
    # not equal method => __ne__
    def  __ne__(object,other):
        if isinstance(object,other.__class__):
            return object.x != other.x and object.y != other.y
    # less Than method =>__lt__
    def  __lt__(object,other):
        if isinstance(object,other.__class__):
            return object.x < other.x or (object.x == other.x and object.y <object.y)
    # HasH =>__hash__
    def __hash__(object):
        return hash(object.x+object.y)

p1 = Point2D(1,2)
p2 = Point2D(2,3)
p6 = Point2D(1,2)


#not equal =>__ne__
# print(p1 != p2)
# print(p1 != p6)

# less Than =>__lt__
# print(p1<p2)
# print(p1<p6)

point_set = set()
point_dict = dict()

point_set.add(p1)


point_dict[p1] = str(p1)
print(point_dict)
