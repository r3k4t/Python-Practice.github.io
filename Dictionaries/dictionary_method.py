'''
# printing values
identity = {'Name':'Ajwad','Age':'21','Job':'Student'}

for i in identity.values():
    print(i)
'''

'''
# printing keys
identity = {'Name':'Ajwad','Age':'21','Job':'Student'}

for i in identity.keys():
    print(i)
'''

'''
#printing items 
identity = {'Name':'Ajwad','Age':'21','Job':'Student'}

for i in identity.items():
    print(i)
'''

'''
identity = {'Name':'Ajwad','Age':'21','Job':'Student'}
x = list(identity.keys())
y = list(identity.values())
print(x)
print(y)
'''

'''
#A handy trick 
identity = {'Name':'Ajwad','Age':'21','Job':'Student'}
for k,v in identity.items():
    print('Key:'+k+' Value:'+v)
'''

'''
#use of 'in' keyword
identity = {'Name':'Ajwad','Age':'21','Job':'Student'}
#It is a dictionary method ==> true
print('Name' in identity)
#It is not a dictionary method ==> false 
print('pop ' in identity)
'''
'''
identity = {'Name':'Ajwad','Age':'21','Job':'Student'}
#It is not a dictionary method ==> false 
print('Tusar' in identity.values())
#It is a dictionary method ==> true
print('Age' in identity.keys())
'''

'''
#the get(key,value/default_value) method
identity = {'Name':'Ajwad','Age':'21','Job':'Student'}
print(str(identity.get('Name','DEFAULT')))
print(str(identity.get('Height','DEFAULT')))
'''

#setdefault()
identity = {'Name':'Ajwad','Age':'21','Job':'Student'}
print(identity.setdefault('Name','Cosmos'))
print(identity.setdefault('Height','6ft'))
print(identity)




