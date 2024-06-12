# -*- coding: utf-8 -*-
from bank.money import Money
from translations import get_translation


class Bank:
    balance = None
    bank_rate = 0.012
    language = 'en'
    currency = 'CNY'

    def __init__(self, config):
        self.bank_rate = config['bank_rate']
        self.balance = Money(config['initial_balance'],config['currency'],config["mark"])
        self.language = config['language']
        self.currency = config['currency']

    def deposit(self, pay_in):
        self.balance += pay_in.amount
        message_template = get_translation('deposit_message', self.language)
        print(message_template.format(amount=pay_in, balance=self.balance))

    def add_interest(self):
        interest = Money(self.balance.amount * (self.bank_rate / 100), self.currency, self.balance.mark)
        self.balance.amount += interest.amount
        message_template = get_translation('interest_message', self.language)
        print(message_template.format(interest=interest, balance=self.balance))

    def withdraw(self, pay_out):
        if self.balance.amount < pay_out.amount:
            self.balance = None
            print(get_translation('insufficient_balance', self.language))
        else:
            self.balance.amount -= pay_out.amount
            message_template = get_translation('withdraw_message', self.language)
            print(message_template.format(amount=pay_out, balance=self.balance))
