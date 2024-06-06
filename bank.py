class Bank:
    balance = 0
    bank_rate = 0.012

    def __init__(self, rate, balance):
        self.bank_rate = rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount:.2f} into account. New balance is {self.balance:.2f}")

    def add_interest(self):
        interest = self.balance * self.bank_rate
        self.balance += interest
        print(f"Added {interest:.2f} interest to account. New balance is {self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = -99
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew { amount:.2f} from account. New balance is {self.balance:.2f}")
