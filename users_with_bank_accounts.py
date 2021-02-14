class User:
    def __init__(self, name, email ):
        self.name = name
        self.email = email
        self.account = bankAccount(0.02, 0)
    def make_deposit(self, amount):
        self.account.balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account.balance -= amount
        return self
    def interest_yield(self):
        self.account.balance += self.account.balance * self.account.interest_rate
        return self
    def display_user_balance(self):
        print(f"{self.name} interest yield is {self.account.interest_rate} and the balance plus interest is {self.account.balance}")
        return self

class bankAccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = int_rate
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawl(self, amount):
        self.balance -= amount
        return self

Cloud = User("Cloud", "Cloud@shinra.com")
Tifa = User("Tifa", "T_fists@shinra.com")


Cloud.make_deposit(100).make_deposit(500).make_deposit(20).make_withdrawl(300).interest_yield().display_user_balance()
Tifa.make_deposit(1000).make_deposit(40).make_withdrawl(40).make_withdrawl(30).make_withdrawl(35).make_withdrawl(20).interest_yield().display_user_balance()