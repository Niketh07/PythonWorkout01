from datetime import datetime
class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def personaldetails(self):
        print(f"Name {self.name}")
        print(f"Country {self.country}")
        print(f"Age {self.agecalc()}")
    def agecalc(self):
        today=datetime.now()
        self.dob=datetime.strptime(self.dob,"%d-%m-%Y")
        age=today.year-self.dob.year-((today.month,today.day)<(self.dob.month,self.dob.day))
        return age
name=input("Enter the name of Employee: ")
country=input("Enter the country of the Employee: ")

while True:
    dob=input("Enter the Date of birth of the Employee in dd-mm-yyyy format: ")
    try:
        dobconverter=datetime.strptime(dob,"%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
    else:
        employee=person(name,country,dob)
        employee.personaldetails()
        break
        

