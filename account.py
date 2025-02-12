class Account:
    # Base class in py
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount, cashback_amount=0):
        if amount > 0 and cashback_amount == 0:
            self.balance += amount
            print(f"Deposited {amount}$. New balance is {self.balance}$.")
        elif amount > 0 and cashback_amount != 0:
            self.balance += (amount + cashback_amount)
            print(f"Deposited {amount}$. New balance is {self.balance}$.")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"withdrew {amount}$. New balance is {self.balance}$.")
        else:
            print("Deposit amount must be positive")

    def display_balance(self):
        print(f"Account balance is {self.balance}$.")


class SavingsAccount(Account):
    # Savings account with interest
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.01):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied {interest}$ interest. New balance is {self.balance}$")

    
class CheckingAccount(Account):
    # Account with no interest
    pass


class HighInterestSavingsAccount(SavingsAccount):
    # Savings account with higher interest
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, holder_name, balance, interest_rate)


class OverdraftCheckingAccount(CheckingAccount):
    # Checking account with overdraft protection
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=500):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"withdrew {amount}$. New balance is {self.balance}$.")
        else:
            print("Deposit amount must be positive")


class PremiumOverdraftCheckingAccount(OverdraftCheckingAccount):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=1000, cashback_rate=0.01):
        super().__init__(account_number, holder_name, balance, overdraft_limit)
        self.cashback_rate = cashback_rate

    def deposit(self, amount):
        cashback = amount * self.cashback_rate
        super().deposit(amount, cashback)
        