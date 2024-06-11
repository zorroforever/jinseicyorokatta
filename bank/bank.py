# -*- coding: utf-8 -*-
from bank.money import Money
from translations import get_translation


class Bank:
    balance = 0
    bank_rate = 0.012
    language = 'en'
    currency = 'CNY'

    def __init__(self, config):
        self.bank_rate = config['bank_rate']
        self.balance = Money(config['initial_balance'],config['currency'],config["mark"])
        self.language = config['language']
        self.currency = config['currency']

    def deposit(self, amount):
        self.balance += amount
        message_template = get_translation('deposit_message', self.language)
        print(message_template.format(amount=amount, balance=self.balance))

    def add_interest(self):
        interest = self.balance.amount * (self.bank_rate / 100)
        self.balance.amount += interest
        message_template = get_translation('interest_message', self.language)
        print(message_template.format(interest=interest, balance=self.balance))

    def withdraw(self, amount):
        if self.balance.amount < amount:
            self.balance = -99
            print(get_translation('insufficient_balance', self.language))
        else:
            self.balance.amount -= amount
            message_template = get_translation('withdraw_message', self.language)
            print(message_template.format(amount=amount, balance=self.balance))
