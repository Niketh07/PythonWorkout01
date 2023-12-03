import math
class shape:
    def __init__(self,side):
        self.side=side
 
 
 class circle(shape):
        def area(self):
            print("This is inside circle function")
            area=[]
            for i in self.side:
                area_c= math.pi*i*i
                area.append(area_c)
            print(f"Area of the cricle with radius {self.side} is {area}")
        def vol(self):
            vol=[]
            for i in self.side:
                vol_c=math.pi*(4/3)*(i*i*i)
                vol.append(vol_c)
            print(f"Area of the cricle with radius {self.side} is {vol}")
# class triangle(shape):    
#     def area(base,height):
#         area_t=0.5*base*height
#         print(f"Volume of the triangle is {area_t}")
#     def vol(base,height):
#         vol_t=base*height
#         print(f"Volume of the triangle is {vol_t}")

class display(circle):
    def __init__(self):
        print("1. Area of Circle\n2. Area of Traingle\n3. Volume of Circle\n4. Volume of Triangle")
        choice=int(input("Enter your choice: "))
        sides=[]
        num=int(input("Enter the number of sides: "))
        print("Enter the length of sides: ")
        for i in range (1,num+1):
            val=int(input())
            sides.append(val)
        match choice:
            case 1:
                print("The sides are",sides)
                #radius=input("Enter the radius of the circle: ")
                super().area(sides)
            # case 2:
            #     radius=input("Enter the radius of the circle: ")
            #     circ.vol(sides)
            case _:
                print("Invalid Input")

call=display()
