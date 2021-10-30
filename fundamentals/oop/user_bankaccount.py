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
        print(f"{User.name}'s Account Balance : ${self.account_balance} ")
        return self
        
    def yield_interest(self):
        if self.account_balance <= 0:
            print(f'No interest earned.')
        else:
            self.account_balance += self.account_balance * self.int_rate 
        return self


class User:		# here's what we have so far
    
    def __init__(self, name, amount):
        self.name = name
        self.account = BankAccount (int_rate=0.01, balance=0)
    # adding the deposit method
    # def make_deposit(self, amount):
    #     self.account.deposit() += amount
    #     return self
    
    # def make_withdrawal(self, amount):
        # self.account.withdraw() -= amount
        # print(self.account.amount)
        # return self

    def display_user_balance(self):
        print(f"{self.name} - ${self.account.account_balance} ")
        return self
    
    # def transfer_money(self, name, amount):
    #     self.account -= amount
    #     self.other_user = name
    #     self.other_user.account += amount
    #     return self

michael = User("Michael", 1000)

teressa = User("Teressa", 5)

jake = User("Jake", 1000000)

michael.account.deposit(300)
michael.display_user_balance()
