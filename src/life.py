import json
from src.util import translations
from src.bank.bank import Bank
from src.cost.fixed_consume import FixedConsume
import argparse

from src.util.output_collector import OutputCollector


def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config


def main(config_path):
    config = load_config(config_path)
    language = config['language']

    try:
        base_year = int(config['base_year'])
        target_year = int(config['target_year'])
        years = int(config['years'])
    except ValueError:
        print(translations.get_translation('Invalid config file.', language))
    if years > 0:
        target_year = base_year + years
        config['target_year'] = target_year
    print(translations.get_translation('start_message', language))
    # init bank account
    my_bank = Bank(config)
    output_collector = OutputCollector(config['output_file_path'])

    no = 0
    for year in range(base_year, target_year):
        no += 1
        print("No.%d:%s%s" % (no, year, '==>'))
        # get interest of bank
        my_bank.add_interest()
        # calculate fixed consume this year
        consume = FixedConsume(config, base_year, year)
        consume.calculate_fixed_consume_yearly()
        # show the result of fixed consume this year
        print(consume.get_no_str())
        # withdraw the fixed consume from bank
        my_bank.withdraw(consume.c_total_consume_yearly)
        # if balance is none, it means My life is over!
        if my_bank.balance is None:
            print(translations.get_translation('life_over', language))
            print('<==')
            output_collector.restore_stdout()
            output_collector.output_to_file()
            return
        print('<== ')
    print(translations.get_translation('end_message', language))
    output_collector.restore_stdout()
    output_collector.output_to_file()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run life.py with a specified config file.")
    parser.add_argument('config_path', type=str, help="Path to the configuration file.")
    args = parser.parse_args()
    main(args.config_path)
