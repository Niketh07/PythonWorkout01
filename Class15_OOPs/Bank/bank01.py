class Transaction:
    global main_bal
    main_bal=0
    def __init__(self,amt):
        self.amt=amt
    def deposit(self):
        main_bal+=self.amt
        print(f"Available Balance is {main_bal}")
    def withdraw(self):
        main_bal-=self.amt
        print(f"Available Balance is {main_bal}")
class Bank(Transaction):
    def __init__(self):
        super(). __init__(self)
    def display(self):
        dep=int(input("Enter the amount to deposit: "))
        self.amt=dep
        super().deposit()

welcome=Bank()
welcome.display()