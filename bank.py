from translations import get_translation


class Bank:
    balance = 0
    bank_rate = 0.012

    def __init__(self, rate, balance, language):
        self.bank_rate = rate
        self.balance = balance
        self.language = language

    def deposit(self, amount):
        self.balance += amount
        message_template = get_translation('deposit_message', self.language)
        print(message_template.format(amount=amount, balance=self.balance))

    def add_interest(self):
        interest = self.balance * self.bank_rate
        self.balance += interest
        message_template = get_translation('interest_message', self.language)
        print(message_template.format(interest=interest, balance=self.balance))

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = -99
            print(get_translation('insufficient_balance', self.language))
        else:
            self.balance -= amount
            message_template = get_translation('withdraw_message', self.language)
            print(message_template.format(amount=amount, balance=self.balance))
