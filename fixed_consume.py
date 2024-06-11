from translations import get_translation


class FixedConsume:
    # custom fees every month, edit by yourself
    # c_house_fee_monthly = 1000
    # c_eng_water_fee_monthly = 50
    # c_eng_electricity_fee_monthly = 200
    # c_eng_air_fee_monthly = 50
    # c_eng_network_fee_monthly = 200
    # c_traffic_fee_monthly = 800
    # c_food_fee_monthly = 3000
    # c_shopping_fee_monthly = 3000
    # c_phone_fee_monthly = 200
    # c_travelling_fee_monthly = 5000
    # c_vip_fee_monthly = 400

    c_insurance_fee_monthly = 0
    c_age = 0
    c_rate = 0
    c_insurance_fee_yearly = 0
    c_total_consume_yearly = 0

    inflation_rate = 0
    birth_year = 0
    retirement_age = 0
    base_year = 0
    target_year = 0
    config = {}

    def __init__(self, config,base_year,target_year):
        self.config = config
        self.language = config['language']
        self.base_year = base_year
        self.inflation_rate = config['inflate_rate']
        self.birth_year = config['birth_year']
        self.retirement_age = config['retirement_age']
        self.target_year = target_year
        self.c_age = self.target_year - self.birth_year

    def inflation_adjustment_factor(self):
        years = self.target_year - self.base_year
        inflation_rate_decimal = self.inflation_rate / 100
        adjustment_factor = (1 + inflation_rate_decimal) ** years
        return adjustment_factor

    def calculate_fixed_consume_yearly(self):
        self.c_rate = self.inflation_adjustment_factor()
        fixed_costs_config = self.config["cost"]["monthly"]["fixed"]
        if fixed_costs_config is None:
            return 0
        fixed_cost = 0
        for key, value in fixed_costs_config.items():
            if key == "insurance_fee" and self.c_age > self.retirement_age:
                continue
            else:
                fixed_cost += value
            if key == "insurance_fee":
                self.c_insurance_fee_monthly = value
        variable_costs_config = self.config["cost"]["monthly"]["variable"]
        variable_costs = 0
        if variable_costs is None:
            return 0
        for key, value in variable_costs_config.items():
            variable_costs += value

        self.c_insurance_fee_yearly = self.c_insurance_fee_monthly * 12 * self.c_rate
        self.c_total_consume_yearly = (fixed_cost + variable_costs) * 12 * self.c_rate
        return self.c_total_consume_yearly

    def get_no_str(self):
        i = self.target_year - self.base_year
        message_template = get_translation('yearly_consumption', self.language)
        return message_template.format(
            age=self.c_age,
            monthly_cost=self.c_total_consume_yearly / 12,
            total_cost=self.c_total_consume_yearly,
            insurance_cost=self.c_insurance_fee_yearly
        )
