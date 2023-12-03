import random
class Transaction:
    global main_bal
    def __init__(self,amt):
        self.amt=amt
    def deposit(self):
        main_bal+=self.amt
        print("Available balance",main_bal)
    def withdraw(self,amt):
        self.amt=amt
        if self.amt>main_bal:
            main_bal-=self.amt
            print("Available balance",main_bal)
        else:
            print("Insufficient Fund")
    def balance(self):
        print(f"Available Balance is {main_bal}")


class Details:
    def accountopening(self):
        name=input("Enter your name: ")
        while True:
            phone_i=int(input("Enter the phone number: "))
            phone=str(phone_i)
            try:
                if len(phone)!=10:
                    print("Enter 10 digits")
                    continue
            except ValueError:
                print("Enter only numbers")
            else:
                break

        print(f"\n Name: {name}\n Phone Number {phone}")
        prefix=146121
        accountno=random.randint(10001,99999)
        accountno_s=str(prefix)+str(accountno)
        accountno_i=int(accountno_s)
        print(f" Account Number: {accountno_i}")


class Bank(Transaction,Details):
    def display(self):
        a=1
        while a==1:
            choice=print("\n\nWelcome to NDK Bank\n1.New Account\n2.Deposit\n3.Withdraw\n4.Balance Equiry")
            choice=int(input("Enter your choice: "))
            match choice:
                case 1:
                    super().accountopening()
                case 2:
                    dep=int(input("Enter the amount to deposit: "))
                    super().deposit(dep)
                    
                case 3:
                    withdraw=int(input("Enter the amount to withdraw: "))
                    super().withdraw(withdraw)
                case 4:
                    print(f"Account No is {super().accountopening()}")
                    print(f"Available balance is {super().balance()}")
                case 5:
                    print("Exit")
                case _:
                    print("Invalid input")

welcome=Bank()
welcome.display()   
                 
              
