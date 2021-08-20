'''
#Class Variables

class StoryBook:

    #Class Variables


    no_of_books = 0

    def __init__(self,name,price,author_name,author_born,no_of_pages):
        #setting the instance variables here

        self.name=name
        self.price =price
        self.author_name = author_name
        self.author_born = author_born
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1





#Creating an instance/object of the Story Book class

book_1 = StoryBook('Hamlet',350,'Shakespeare',1564,500)
book_2 = StoryBook('the_kite_runner',200,'khaled_hosseini',1965,200)




print(book_1.no_of_books)
print(book_2.no_of_books)
print(StoryBook.no_of_books)
'''

'''
class StoryBook:

    #Class Variables


    no_of_books = 0

    discount = 0.5

    def __init__(self,name,price,author_name,author_born,no_of_pages):
        #setting the instance variables here

        self.name=name
        self.price =price
        self.author_name = author_name
        self.author_born = author_born
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1

    def apply_discount(self):
        self.price = int(self.price - self.price * self.discount)



#Creating an instance/object of the Story Book class

book_1 = StoryBook('Hamlet',350,'Shakespeare',1564,500)
book_2 = StoryBook('the_kite_runner',200,'khaled_hosseini',1965,200)



print(book_2.price)
book_2.discount = 0.3
book_2.apply_discount()
print(book_2.price)
'''
class StoryBook:

    #Class Variables


    no_of_books = 0

    discount = 0.5

    def __init__(self,name,price,author_name,author_born,no_of_pages):
        #setting the instance variables here

        self.name=name
        self.price =price
        self.author_name = author_name
        self.author_born = author_born
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1

    def apply_discount(self):
        self.price = int(self.price - self.price * StoryBook.discount)



#Creating an instance/object of the Story Book class

book_1 = StoryBook('Hamlet',350,'Shakespeare',1564,500)
book_2 = StoryBook('the_kite_runner',200,'khaled_hosseini',1965,200)



print(book_2.price)
book_2.discount = 0.3
book_2.apply_discount()
print(book_2.price)
