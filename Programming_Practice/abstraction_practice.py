"""
Create Account class with 2 Attributes-Balance and Account no.
Create methods for debit, credit and printing the balance
"""


class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("RS.", amount, "is debited.")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("RS.", amount, "is credited.")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(15000, 123456)
print(acc1.balance)
print(acc1.acc_no)
acc1.debit(1000)
acc1.credit(2000)
