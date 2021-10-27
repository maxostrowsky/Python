
# pseudo code
# x 1. create class user (add attributes)
# x 2. dunder init and make_desposit methods made
# x 3. add a make_withdrawal method
# x 4. Create 3 instances of the user class
# x 5. make display_user_balance 
# x 6. Have the first user make 3 deposits and 1 withdrawal and then display their balance
# x 7. Have the second user make 2 deposits and 2 withdrawals and then display their balance
# x 8. Have the third user make 1 deposits and 3 withdrawals and then display their balance
# x BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances



class User:		# here's what we have so far
    
    def __init__(self, name, amount):
        self.name = name
        self.account_balance = amount
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name} - ${self.account_balance} ")
        return self
    
    def transfer_money(self, name, amount):
        self.account_balance -= amount
        self.other_user = name
        self.other_user.account_balance += amount
        return self


michael = User("Michael", 1000)

teressa = User("Teressa", 5)

jake = User("Jake", 1000000)

michael.make_deposit(100).make_deposit(1).make_deposit(1).make_withdrawal(3.33)

teressa.make_deposit(500).make_withdrawal(125.36).make_deposit(600).make_withdrawal(2225.01)

jake.make_withdrawal(97.54).make_withdrawal(1.50).make_withdrawal(14.99).make_deposit(40000000)

michael.display_user_balance()
teressa.display_user_balance()
jake.display_user_balance()

michael.transfer_money(teressa, 200).display_user_balance()
teressa.display_user_balance()