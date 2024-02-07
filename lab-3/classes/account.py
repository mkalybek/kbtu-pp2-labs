class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

account = Account("Vanya", 500)
account.withdraw(100)
account.deposit(10)
account.withdraw(1000)
