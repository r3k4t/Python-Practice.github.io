'''
class StoryBook:
    
    def __init__(self):
        print( "I am being called with instance/object creation")
        

# Creating  an instance/object of the StoryBook Class    
book_1 = StoryBook()
book_2 = StoryBook()
'''

'''
class StoryBook:
    
    
    def __init__(self,name,price,author_name,author_born):
        #setting the instance variables here
        self.name = name
        self.price = price
        self.author_name= author_name
        self.author_born = author_born
        


# Creating  an instance/object of the StoryBook Class    
book_1 = StoryBook('Hamlet',350,'Shakespeare',1564)
book_2 = StoryBook('the_kite_runner',200,'Khaled_Hosseini',1965)


print(book_1.name)
print(book_1.price)
print(book_1.author_name)
print(book_1.author_born)

print(book_2.name)
print(book_2.price)
print(book_2.author_name)
print(book_2.author_born)
'''


'''
#Change the name variable
class StoryBook:
    
    
    def __init__(self,name,price,author_name,author_born):
        #setting the instance variables here
        self.name = name
        self.price = price
        self.author_name= author_name
        self.author_born = author_born
        


# Creating  an instance/object of the StoryBook Class    
book_1 = StoryBook('Hamlet',350,'Shakespeare',1564)
book_2 = StoryBook('the_kite_runner',200,'Khaled_Hosseini',1965)
book_1.name = 'lolipop'



print(book_1.name)
print(book_2.price)
'''

class StoryBook:
    
    
    def __init__(self,name,price,author_name,author_born):
        #setting the instance variables here
        self.name = name
        self.price = price
        self.author_name= author_name
        self.author_born = author_born
        self.publishing_year = 2020
        


# Creating  an instance/object of the StoryBook Class    
book_1 = StoryBook('Hamlet',350,'Shakespeare',1564)
book_2 = StoryBook('the_kite_runner',200,'Khaled_Hosseini',1965)



print(book_1.publishing_year)
#print(book_2.price)


