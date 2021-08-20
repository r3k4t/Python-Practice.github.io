 #old way of formatting string -- C style 
 
 #print('I am '%s 'tusar')
 #print('I am %s and %d years old' % ('tusar',23))
 
 #name = 'mark'
 #age = 23
 #professional = 'Player'
 #earning = 245000.344
 
#print('I am %s and I am %d years old.I am an %s and I earn %.2f$' %(name,age,professional,earning))

'''
#A slightly better way of formatting strings,introduction in python 2.6

print(' I am {} and I am {}'.format('tusar','happy'))

tu = (12,45,22222,103,6)
print ( '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu))

'''

'''
# A much better way to formatting strings,introduced in python3 and above

food = 'sandwich'
language='python'
name = 'Tusar'
print(f'I  am {name} and I eat {food}.I don\'t believe in {language} haters\nAnd {2**2} == {4}')
'''