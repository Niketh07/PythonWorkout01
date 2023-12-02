class calculator:
    def __init__(self,num1,num2):
        self.n1=num1
        self.n2=num2
        def add(self):
            print(f"Sum of {self.n1} and {self.n2} is {self.n1+self.n2}")
    def diff(self):
        print(f"Difference of {self.n1} and {self.n2} is {self.n1-self.n2}")
    def mult(self):
        print(f"Product of {self.n1} and {self.n2} is {self.n1*self.n2}")
    def div(self):
        print(f"Quotient of {self.n1} and {self.n2} is {self.n1/self.n2}")

print("Choose the Arithmetic Operation from the below list")
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
choice=int(input("Enter your choice: "))
numeric1=int(input("Enter the first number: "))
numeric2=int(input("Enter the second number: "))
operation=calculator(numeric1,numeric2)
match choice:
    case 1:
        operation.add()
    case 2:
        operation.diff()
    case 3:
        operation.mult()
    case 4:
        operation.div()
    case _:
        print("Invalid Choice")