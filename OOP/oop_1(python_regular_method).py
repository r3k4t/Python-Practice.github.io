class StoryBook:
    
    
   
    def __init__(self,name,price,author_name,author_born,no_of_pages):
        #setting the instance variables here
        
        self.name=name
        self.price =price
        self.author_name = author_name
        self.author_born = author_born
        self.no_of_pages = no_of_pages
        
    # Regular method 
    def get_book_info(self):
        print(f'The book name:{self.name},price:{self.price},pages:{self.no_of_pages}')
        
    def get_author_info(self):
        print(f'The author name:{self.author_name},born:{self.author_born}')
        
    
#Creating an instance/object of the Story Book class

book_1 = StoryBook('Hamlet',350,'Shakespeare',1564,500)
book_2 = StoryBook('the_kite_runner',200,'khaled_hosseini',1965,200)

         
book_1.get_book_info()
StoryBook.get_author_()

