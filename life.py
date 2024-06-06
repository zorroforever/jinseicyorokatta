import translations
from bank import Bank
from fixed_consume import FixedConsume





if __name__ == '__main__':
    # Language selection
    language = input("Select language (en/zh/ja): ").strip()
    print(translations.get_translation('start_message', language))
    # init bank account
    my_bank = Bank(0.0012, 50000000,language)
    base_year = 2024
    target_year = 2084
    inflate_rate = 4.48
    birth_year = 1983
    retirement_age = 65

    for year in range(base_year, target_year):
        # get interest of bank
        my_bank.add_interest()
        # calculate fixed consume this year
        consume = FixedConsume(base_year, year, inflate_rate, birth_year, retirement_age,language)
        consume.calculate_fixed_consume_yearly()
        # show the result of fixed consume this year
        print(consume.get_no_str())
        # withdraw the fixed consume from bank
        my_bank.withdraw(consume.c_total_consume_yearly)
        # if balance is -99, it means My life is over!
        if my_bank.balance == -99:
            print(translations.get_translation('life_over', language))
            break
