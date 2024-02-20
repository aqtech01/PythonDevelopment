import gradio as gr


class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return f"Account Number = {self.account_number} \n Account Title = {self.account_holder} \n Account Balance = {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        if amount < self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(self.balance)


class SavingAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"{super().__str__()} \n Interest Rate is {self.interest_rate} "

    def interest_calc(self, time):
        p = self.balance
        interset_calculator = p * self.interest_rate * time
        self.balance += interset_calculator



def main():
    account_title = input("Enter Account Title: ")
    account_number = int(input("Enter Account Number: "))
    balance = float(input("Enter Account Balance: "))
    interest_rate = float(input("Enter Interest Rate: "))
    time = int(input("Enter Time (in years): "))

    obj = SavingAccount(account_number, account_title, balance, interest_rate)
    obj.interest_calc(time)
    print(obj)


if __name__ == "__main__":
    main()

# iface = gr.Interface(fn=SavingAccount,
#                      inputs=["text", "number", "number", "number", "number"],
#                      outputs="text",
#                      inputs_label=["Account Title", "Account Number", "Initial Balance", "Interest Rate", "Time (in "
#                                                                                                           "years)"],
#                      outputs_label="Account Information",
#                      title="Saving Account Information Calculator",
#                      description="Enter your account details to calculate final balance after interest.")
#
# iface.launch()
