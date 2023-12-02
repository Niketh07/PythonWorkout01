import math
class circle:
    def __init__(self,radius):
          self.rad=radius
    def area(self):
         print(f"Area of circle is {round(2*math.pi*(self.rad**2),2)}")
    def perimeter(self):
         print(f"Perimeter of circle is {round((2*math.pi*self.rad),2)}")

r=int(input("Enter the radius of the circle: "))
value=circle(r)
value.area()
value.perimeter()

