import random
class AccountOpening:
    accntno= 14210+random.randrange(10001,99999)
    def __init__(self):
        name=input("Enter your name: ")
        while True:
            phone=int(input("Enter mobile number: "))
            try:
                if len(phone)!=10:
                    print("Enter 10 digitis ")
                    continue
            except ValueError:
                print("Enter only number ")
                continue
            else:
                break
        print("\nAccount Details","\nName: ",name,"\nPhone Number: ",phone)
       
        print(f"Your Acount Number is : 1421000{AccountOpening.accntno}")

class Transaction:
    main_bal=0
    def __init__(self,deposit,withdraw):
            self.deposit=deposit
            self.withdraw=withdraw
    def dep(self):
         Transaction.main_bal+=self.deposit
         print("Available balance is ",Transaction.main_bal)
    def withd(self):
         print(f"{Transaction.main_bal} is the availble balance")
         if self.withdraw<=Transaction.main_bal:
              Transaction.main_bal=Transaction.main_bal-self.withdraw
              print(f"Thank you for banking.\nAvailable balance is {Transaction.main_bal}")
         else:
              print("Insufficient Fund")

a=1
while a==1:
    print("\n\nWelcome to NDK Bank\n1.New Account\n2.Deposit\n3.Withdraw\n4.Balance Equiry")
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            AccountOpening()
        case 2:
            withdraw=0
            dep=int(input("Enter the amount to deposit: "))
            deposit=Transaction(dep,withdraw)
            deposit.dep()
        case 3:
            withdraw=int(input("Enter the amount to withdraw: "))
            withdraw=Transaction(Transaction.main_bal,withdraw)
            withdraw.withd()
        case 4:
            print(f"Account No is {AccountOpening.accntno}")
            print(f"Available balance is {Transaction.main_bal}")
        case 5:
            print("Exit")
            break
        case _:
            print("Invalid input")                                              

