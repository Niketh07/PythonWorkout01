class person:
    def __init__(self,firstname,lastname):
        self.fname=firstname
        self.lname=lastname
    
    def display(self):
        print("First Name is ",self.fname,"\nLAst Name is ",self.lname,"\nAge is",self.age)

class minor(person):
    def __init__(self,firstname,lastname):
        person.__init__(self,firstname,lastname) #this implies that the init in parent should be used here also

class major(person):
    def __init__(self,firstname,lastname,age):
        #When using super function
        super().__init__(firstname,lastname) #no need to give self in super function
        self.age=age

#once connection between parent is child is done we need to create object with the child

x=minor("Sagar","Jacky")
x.display()

y=major("Donald","John",45)
y.display()
