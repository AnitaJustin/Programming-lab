class bank_account:
    def __init__(self,accountnumber,name,type_of_account,balance):
        self.accountno=accountnumber
        self.name=name
        self.type=type_of_account
        self.balance=balance

    def deposit(self):
        self.balance+=int(input("enter the amount deposit"))
        print("current balance:",self.balance)
    def withdraw(self):
        self.balance-=int(input("enter the amount to withdraw"))
        print("current balance:",self.balance)
        
acc=bank_account(int(input("enter the bank account number")),input("enter the name"),("enter the type of account"),int(input("enter the accountbalance")))
acc.deposit()
acc.withdraw()
