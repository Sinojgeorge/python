class bank():
    def __init__(self):
        self.accno=int(input("Enter your account number:"))
        self.acctypr=input("enter account type:")
        self.holdname=input("Enter account holders name:")
        self.balance=int(input("Enter account balance:"))
    def deposit(self):
        amount=int(input("Enter the amount to deposit:"))
        self.balance+=amount
        print("The account balanceis :",self.balance)
    def withdraw(self):
        amount=int(input("enter the amount to withdraw:"))
        if self.balance>=amount:
         self.balance-=amount
         print("you have withdrawn",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("Net available balance is",self.balance)
a=bank()
a.deposit()
a.withdraw()
a.display()
