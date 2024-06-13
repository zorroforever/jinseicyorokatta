# -*- coding: utf-8 -*-
from util.translations import get_translation


class Money:
    amount = 0
    currency = "CNY"
    mark = "¥"
    language = "en"
    exchange_rates = {
        ("CNY", "USD"): 0.15,
        ("USD", "CNY"): 6.65,
        ("CNY", "JPY"): 21.667,
        ("JPY", "CNY"): 0.046,
        ("USD", "JPY"): 156.85,
        ("JPY", "USD"): 0.0064,
        # Add more exchange rates as needed
    }

    def __init__(self, amount, currency="CNY", mark="¥",language="en"):
        self.amount = amount
        self.currency = currency
        self.mark = mark
        self.language = language

    def __str__(self):
        return f"{self.mark}{self.amount}"

    def __format__(self, format_spec):
        return f"{self.mark}{self.amount:{format_spec}}"

    @staticmethod
    def get_exchange_rate(from_currency, to_currency):
        if from_currency == to_currency:
            return 1
        return Money.exchange_rates.get((from_currency, to_currency), None)

    def convert_to(self, target_currency):
        if self.currency == target_currency:
            return Money(self.amount, self.currency, self.mark)
        rate = self.get_exchange_rate(self.currency, target_currency)
        if rate is None:
            message = get_translation("no_exchange_rate",self.language).format(self.currency, target_currency)
            raise ValueError(message)
        target_mark = {"CNY": "¥", "USD": "$", "JPY": "¥"}.get(target_currency, "")
        return Money(self.amount * rate, target_currency, target_mark)

    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                other = other.convert_to(self.currency)
            return Money(self.amount + other.amount, self.currency, self.mark)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency, self.mark)
        else:
            message = get_translation("unsupported_type",self.language).format(type(other).__name__)
            raise TypeError(message)

    def __sub__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                other = other.convert_to(self.currency)
            return Money(self.amount - other.amount, self.currency, self.mark)
        elif isinstance(other, (int, float)):
            return Money(self.amount - other, self.currency, self.mark)
        else:
            message = get_translation("unsupported_type",self.language).format(type(other).__name__)
            raise TypeError(message)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency, self.mark)
        else:
            message = get_translation("unsupported_type",self.language).format(type(other).__name__)
            raise TypeError(message)

    def __rmul__(self, other):
        return self.__mul__(other)  # Make multiplication commutative

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                message = get_translation("division_by_zero",self.language)
                raise ValueError(message)
            return Money(self.amount / other, self.currency, self.mark)
        else:
            message = get_translation("unsupported_type",self.language).format(type(other).__name__)
            raise TypeError(message)

    def __rtruediv__(self, other):
        message = get_translation("number_divided_by_money",self.language)
        raise TypeError(message)

    def __neg__(self):
        return Money(-self.amount, self.currency, self.mark)

    def __abs__(self):
        return Money(abs(self.amount), self.currency, self.mark)

    def __eq__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                other = other.convert_to(self.currency)
            return self.amount == other.amount
        elif isinstance(other, (int, float)):
            return self.amount == other
        return False

    def __lt__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                other = other.convert_to(self.currency)
            return self.amount < other.amount
        elif isinstance(other, (int, float)):
            return self.amount < other
        else:
            message = get_translation("unsupported_type",self.language).format(type(other).__name__)
            raise TypeError(message)

    def __le__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                other = other.convert_to(self.currency)
            return self.amount <= other.amount
        elif isinstance(other, (int, float)):
            return self.amount <= other
        else:
            message = get_translation("unsupported_type", self.language).format(type(other).__name__)
            raise TypeError(message)

    def __gt__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                other = other.convert_to(self.currency)
            return self.amount > other.amount
        elif isinstance(other, (int, float)):
            return self.amount > other
        else:
            message = get_translation("unsupported_type", self.language).format(type(other).__name__)
            raise TypeError(message)

    def __ge__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                other = other.convert_to(self.currency)
            return self.amount >= other.amount
        elif isinstance(other, (int, float)):
            return self.amount >= other
        else:
            message = get_translation("unsupported_type", self.language).format(type(other).__name__)
            raise TypeError(message)

    def __repr__(self):
        return f"Money(amount={self.amount}, currency='{self.currency}', mark='{self.mark}')"
