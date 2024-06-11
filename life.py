import json
import translations
from bank.bank import Bank
from fixed_consume import FixedConsume

if __name__ == '__main__':

    # Read configuration from file
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    bank_rate = config['bank_rate']
    initial_balance = config['initial_balance']
    base_year = config['base_year']
    if config['years'] > 0:
        target_year = base_year + config['years']
    else:
        target_year = config['target_year']
        config['target_year'] = target_year

    language = config['language']
    print(translations.get_translation('start_message', language))
    # init bank account
    my_bank = Bank(config)
    no = 0
    for year in range(base_year, target_year):
        no += 1
        print("No.%d:%s%s" % (no,year,'==>'))
        # get interest of bank
        my_bank.add_interest()
        # calculate fixed consume this year
        consume = FixedConsume(config,base_year,year)
        consume.calculate_fixed_consume_yearly()
        # show the result of fixed consume this year
        print(consume.get_no_str())
        # withdraw the fixed consume from bank
        my_bank.withdraw(consume.c_total_consume_yearly)
        # if balance is -99, it means My life is over!
        if my_bank.balance == -99:
            print(translations.get_translation('life_over', language))
            print( '<==')
            break
        print('<== ')
    print(translations.get_translation('end_message', language))