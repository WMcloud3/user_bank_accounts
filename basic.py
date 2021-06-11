class BankAccount:
    bank_name = "Ninja Savings and Loans"
    def __init__(self, account_interest = 0.02, account_balance = 0):
        self.account_interest = account_interest
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance += amount
        print(self.account_balance)
    def withdraw(self, amount):
        if self.account_balance - amount >= 0:
            self.account_balance - amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance - 5
    def display_account_info(self):
        print(self.account_balance)
    def yield_interest(self):
        if self.account_balance > 0:
            int_yeld = self.account_balance * self.account.account_interest
            self.account_balance = self.account_balance + int_yeld

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account.balance = BankAccount(account_interest, balance)
    def make_deposit(self, amount):
        self.acount.deposit(amount)
    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
    def display_user_balance(self, balance):
        self.account.display_account_info