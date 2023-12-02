#many forms, commonly used in class methods, 
#i.e there will be multiple class names but with same method name

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self): #self is used to access all the variables
        print("\nThis display is the function inside the student class")
    

class adult:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self): 
        print("\nThis display is the function inside the adult class")

class major:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self): 
        print("\nThis display is the function inside the major class")

objstd=student("Becham",37)
objadult=adult("Sam",30)
objmajor=major("Ram",24)

# Calling the funcitons indivisually
# objstd.display()
# objadult.display()
# objmajor.display()

#Calling the function using a for loop
for i in (objstd,objadult,objmajor):
    i.display()