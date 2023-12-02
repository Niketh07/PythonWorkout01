#Inheritance
class student: #parent class
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self): #self is used to access all the variables
        print("\nThis display is the function inside the student class")
    

class adult(student): #no need of init method for the child class
    def display(self): 
        print("\nThis display is the function inside the adult class")

class major(student):
    def display(self): 
        print("\nThis display is the function inside the major class")

objstd=student("Becham",37)
objadult=adult("Sam",30)
objmajor=major("Ram",24)


#Calling the function using a for loop
for i in (objstd,objadult,objmajor):
    i.display()