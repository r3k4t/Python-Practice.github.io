class StoryBook:
    pass

# creating an instance/object of the StoryBook Class
book_1 = StoryBook()
book_2 = StoryBook()
#print(book_1)
#print(StoryBook)


# instance variable
book_1.name='Hamlet'
book_1.price = 350
book_1.author_name = 'Shakespare'
book_1.author_born= 1564

book_2.name='the_kite_runner'
book_2.price = 200
book_2.author_name = 'khaled_hosseni'
book_2.author_born= 1965

print(book_1.name)
print(book_2.name)