class BankAccount:
    def __init__(self, balance=0, intRate=0.01):
        self.balance = balance
        self.intRate = intRate
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdrawal(self, amount):
        if(self.balance-amount>0):
            self.balance=self.balance - amount
        else:
            print(f"{self.balance} You do not have enough money in your account to make a withdrawal")
    def display_account_info(self):
        print(f"You have a balance of ${self.balance}")
    # def yield_interest(self, years):
    #     self.balance = self.balance+(self.intRate/self.balance*years)

Acct1 = BankAccount(100, .01)

class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account
    
    # other methods
    
    def make_deposit(self, amount):
        self.deposit(amount)
    def make_withdrawal(self, amount):
        self.withdrawal(amount)
    def display_users_account_balance(self):
        self.display_account_info()


Acct1_User = User("Bob", "Bob@gmail.com", Acct1)

print(Acct1.balance)
Acct1.deposit(100)
print(Acct1.balance)
Acct1.withdrawal(100)
print(Acct1.balance)
Acct1.withdrawal(300)
print(Acct1.balance)
Acct1.display_account_info()
