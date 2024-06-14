from ..bank.money import Money
from src.util.translations import get_translation


class FixedConsume:
    c_age = 0
    c_rate = 0
    c_insurance_fee_monthly = 0
    c_insurance_fee_yearly = 0
    c_total_consume_monthly = 0
    c_total_consume_yearly = 0

    inflation_rate = 0
    birth_year = 0
    retirement_age = 0
    base_year = 0
    target_year = 0
    config = {}
    currency = ""

    def __init__(self, config, base_year, target_year):
        self.config = config
        self.language = config['language']
        self.base_year = int(base_year)
        self.inflation_rate = float(config['inflate_rate'])
        self.birth_year = int(config['birth_year'])
        self.retirement_age = int(config['retirement_age'])
        self.target_year = int(target_year)
        self.c_age = self.target_year - self.birth_year
        self.currency = config['currency']
        self.mark = config['mark']

    def inflation_adjustment_factor(self):
        years = self.target_year - self.base_year
        inflation_rate_decimal = self.inflation_rate / 100
        adjustment_factor = (1 + inflation_rate_decimal) ** years
        return adjustment_factor


    def calculate_fixed_consume_yearly(self):
        self.c_rate = self.inflation_adjustment_factor()
        fixed_cost = 0
        variable_costs = 0
        annual_costs = 0
        try:
            fixed_costs_config = self.config["cost"]["monthly"]["fixed"]
            if fixed_costs_config is not None:
                for key, value in fixed_costs_config.items():
                    if key == "insurance_fee" and self.c_age > self.retirement_age:
                        continue
                    else:
                        fixed_cost += float(value)
                    if key == "insurance_fee":
                        self.c_insurance_fee_monthly = float(value)
        except KeyError:
            fixed_cost = 0
        try:
            variable_costs_config = self.config["cost"]["monthly"]["variable"]
            if variable_costs is not None:
                for key, value in variable_costs_config.items():
                    variable_costs += float(value)
        except KeyError:
            variable_costs = 0
        try:
            annual_costs_config = self.config["cost"]["monthly"]["annual"]
            if annual_costs is not None:
                for key, value in annual_costs_config.items():
                    annual_costs += float(value)
        except KeyError:
            annual_costs = 0
        self.c_insurance_fee_yearly = Money(self.c_insurance_fee_monthly * 12 * self.c_rate, self.currency, self.mark)
        self.c_total_consume_yearly = Money((fixed_cost + variable_costs + annual_costs) * 12 * self.c_rate, self.currency, self.mark)
        self.c_total_consume_monthly = Money((fixed_cost + variable_costs + annual_costs) * self.c_rate, self.currency, self.mark)
        return self.c_total_consume_yearly

    def get_no_str(self):
        message_template = get_translation('yearly_consumption', self.language)
        return message_template.format(
            age=self.c_age,
            monthly_cost=self.c_total_consume_monthly,
            total_cost=self.c_total_consume_yearly,
            insurance_cost=self.c_insurance_fee_yearly
        )
