#This program counts the frequency of characters on a string.

'''

text = "This is a simple text to TEST the code."

letters = {}

for i in text:
    letters.setdefault(i,0)
    letters[i]=letters[i]+1
    
print(letters)
'''


'''
#pprint --> Data pretty printer
import pprint as pp
text = "This is a simple text to TEST the code."

letters = {}

for i in text:
    letters.setdefault(i,0)
    letters[i]=letters[i]+1
    
pp.pprint(letters)
'''