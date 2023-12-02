#Non parameterised constructor
class Student():
    def __init__(self): # This is a non parameterized constructor
        print("\nThis is a non parameterized constructor")
    
    def display(self,name):
        self.name=name
        print("Student name is ",self.name)   
std=Student()
std.display("John") 


#Parameterized constructor
class car():
    def __init__(self,brand): # This is a parameterized constructor
        self.brand=brand
        print("\nParameterised Constructor\nThis car brand is ",brand)
    
    def display(self):
   
        print("This is a sample function with parameter is passed in the constructor\n")   
carbrand=car("Honda")
carbrand.display() 