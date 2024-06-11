# -*- coding: utf-8 -*-
class Money:
    amount = 0
    currency = "CNY"
    mark = "¥"

    def __init__(self, amount, currency="CNY", mark="¥"):
        self.amount = amount
        self.currency = currency
        self.mark = mark

    def __str__(self):
        return f"{self.mark}{self.amount}"

    def __format__(self, format_spec):
        return f"{self.mark}{self.amount:{format_spec}}"