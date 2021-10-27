class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0):
        self.int_rate = 0.01
        self.account_balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance < amount:
            print(f"Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5 + amount
        else: 
            self.account_balance -= amount
        return self
        
        
    def display_account_info(self):
        print(f"Account Balance : ${self.account_balance} ")
        return self
        
    def yield_interest(self):
        if self.account_balance <= 0:
            print(f'No interest earned.')
        else:
            self.account_balance += self.account_balance * self.int_rate 
        return self

checking = BankAccount('0.01', 0)

savings =BankAccount('0.01', 1000)

checking.deposit(1000).deposit(525).deposit(122.25).withdraw(400.01).yield_interest().display_account_info()

savings.deposit(10000).deposit(1550.26).withdraw(1000).withdraw(200.27).withdraw(1030).withdraw(2002).yield_interest().display_account_info()