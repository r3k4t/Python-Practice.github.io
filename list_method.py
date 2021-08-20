places_visited = ['India','Nepal','Malaysia','Bhutan','USA','ak','bk']

# the  list methods
# the index() method

# print(places_visited.index('Bhutan'))

# the append()

# places_visited.append('Africa')
# print(places_visited)

# the insert()
# places_visited.insert(2,'United Kingdom')
# print(places_visited)

# the remove()
# places_visited.remove('Nepal')
# print(places_visited)

# sort()
# places_visited.sort()
# print(places_visited)

# places_visited.sort(key = str.lower)
# print(places_visited)

places_visited.sort(key = str.lower,reverse=True)
print(places_visited)