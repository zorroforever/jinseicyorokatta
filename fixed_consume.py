class FixedConsume:
    # custom fees every month, edit by yourself
    c_house_fee_monthly = 1000
    c_eng_water_fee_monthly = 50
    c_eng_electricity_fee_monthly = 200
    c_eng_air_fee_monthly = 50
    c_eng_network_fee_monthly = 200
    c_traffic_fee_monthly = 800
    c_food_fee_monthly = 3000
    c_shopping_fee_monthly = 3000
    c_phone_fee_monthly = 200
    c_insurance_fee_monthly = 4000
    c_travelling_fee_monthly = 5000
    c_vip_fee_monthly = 400

    c_age = 18
    c_rate = 1
    c_insurance_fee_yearly = 0
    c_total_consume_yearly = 0

    inflation_rate = 0
    birth_year = 0
    retirement_age = 0
    base_year = 0
    target_year = 0

    def __init__(self, base_year, target_year, inflate_rate, birth_year, retirement_age):
        self.base_year = base_year
        self.inflation_rate = inflate_rate
        self.birth_year = birth_year
        self.retirement_age = retirement_age
        self.target_year = target_year
        self.c_age = self.target_year - self.birth_year
        if self.c_age > self.retirement_age:
            self.c_insurance_fee_monthly = 0

    def inflation_adjustment_factor(self):
        years = self.target_year - self.base_year
        inflation_rate_decimal = self.inflation_rate / 100
        adjustment_factor = (1 + inflation_rate_decimal) ** years
        return adjustment_factor

    def calculate_fixed_consume_yearly(self):
        self.c_rate = self.inflation_adjustment_factor()
        fixed_consume = (self.c_house_fee_monthly
                         + self.c_eng_water_fee_monthly
                         + self.c_eng_electricity_fee_monthly
                         + self.c_eng_air_fee_monthly
                         + self.c_eng_network_fee_monthly
                         + self.c_traffic_fee_monthly
                         + self.c_food_fee_monthly
                         + self.c_shopping_fee_monthly
                         + self.c_phone_fee_monthly
                         + self.c_travelling_fee_monthly
                         + self.c_vip_fee_monthly
                         + self.c_insurance_fee_monthly)
        self.c_insurance_fee_yearly = self.c_insurance_fee_monthly * 12 * self.c_rate
        self.c_total_consume_yearly = fixed_consume * 12 * self.c_rate
        return self.c_total_consume_yearly

    def get_no_str(self):
        i = self.target_year - self.base_year
        return f"No.{ i + 1}|{self.base_year + i},age:{self.c_age},monthly_insurance_cost={(self.c_total_consume_yearly / 12):.2f},total_consume={self.c_total_consume_yearly:.2f},yearly_insurance_cost={self.c_insurance_fee_yearly:.2f}"

