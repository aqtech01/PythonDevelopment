class Account:
    def __init__(self, account_num, account_title, balance):
        self.account_num = account_num
        self.account_title = account_title
        self.balance = balance

    def __str__(self):
        return f"Account Number : {self.account_num} , Title : {self.account_title} , Balance:{self.balance}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")


a1 = Account(101, "AQTECH", 1001)
a2 = Account(102, "Tanveer", 1002)
print(a1)
a1.deposit(600)
print(a1)
a1.withdraw(200)
print(a1)
print("<-------------------->")
print(a2)
