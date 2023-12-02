from abc import ABC

# polygon Child class of Abstractclass - hidden functionalty abc=> Abstract Class
#We dont call an abstract class in a program
class polygon(ABC):
    def sides(self):
        pass

class triangle(polygon):
    def sides(self):
        print("3 sides")
    
class circle(polygon):
    def sides(self):
        print("rounded")
class rectangle(polygon):
    def sides(self):
        print("4 sides")

#object creation
objtriangle=triangle()
objtriangle.sides()

objcircle=circle()
objcircle.sides()

objrectangle=rectangle()
objrectangle.sides()