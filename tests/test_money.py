from flask_app import parse_nested_form
from src.bank.money import Money


class TestMoney:
    def test_add(self):
        a = Money(10, 'USD', "$")
        b = Money(20, 'USD', "$")
        assert a + b == Money(30, 'USD', "$")

    def test_sub(self):
        a = Money(10, 'USD', "$")
        b = Money(20, 'USD', "$")
        assert a - b == Money(-10, 'USD', "$")

    def test_mul(self):
        a = Money(10, 'USD', "$")
        assert a * 11.1 == Money(111, 'USD', "$")

    def test_add2(self):
        a = Money(10, 'USD', "$","ja")
        assert a + 1 == Money(11, 'USD', "$")

    def test_compare(self):
        a = Money(10.98, 'USD', "$")
        if a >= 10:
            assert True
        else:
            assert False

    def test_compare2(self):
        config_data = {'language': ["['zh']"], 'currency': ["['CNY']"], 'mark': ["['¥']"], 'bank_rate': ["['1.2']"], 'initial_balance': ["['50000000']"], 'base_year': ["['2024']"], 'years': ["['30']"], 'target_year': ["['2084']"], 'inflate_rate': ["['4.48']"], 'birth_year': ["['1983']"], 'retirement_age': ["['65']"], 'output_file_path': ["['out.txt']"], 'cost.monthly.fixed.house_fee': ["['1000']"], 'cost.monthly.fixed.eng_water_fee': ["['50']"], 'cost.monthly.fixed.eng_electricity_fee': ["['200']"], 'cost.monthly.fixed.eng_gas_fee': ["['50']"], 'cost.monthly.fixed.eng_network_fee': ["['200']"], 'cost.monthly.fixed.phone_fee': ["['200']"], 'cost.monthly.fixed.insurance_fee': ["['4000']"], 'cost.monthly.variable.traffic_fee': ["['800']"], 'cost.monthly.variable.food_fee': ["['3000']"], 'cost.monthly.variable.shopping_fee': ["['3000']"], 'cost.monthly.variable.travelling_fee': ["['5000']"], 'cost.monthly.variable.vip_fee': ["['400']"]}
        nested_data = parse_nested_form(config_data)
        print(nested_data)