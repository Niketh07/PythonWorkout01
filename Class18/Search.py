import re

mystring="This is a sample text for creating search pattern"
#findall()
import re

patterns = '^a(b*)$'
test_string = 'abyss'
result = re.match(patterns, test_string)



x=re.findall("te",mystring)
print(x)

y=re.findall("ra",mystring) #if it is not matching we will get an empty list
print(y)

#search()
z=re.search("\s",mystring) #\s will search for white spaces
print(z.start())#this will returnat staring where do we have white spaces here it is after this ie 4 letters

#split()
d=re.split("\s",mystring) 
print(d)

#sub()
e=re.sub("text","string",mystring)
print(e)