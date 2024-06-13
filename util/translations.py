# -*- coding: utf-8 -*-
supported_languages = ['en', 'zh', 'ja']
translations = {
    'start_message': {
        'en': "Life is easy, start!",
        'zh': "人生,易如翻掌！　开始吧！",
        'ja': "人生、チョロかった！　スタート！"
    },
    'end_message': {
        'en': "Life is easy, to be continued!",
        'zh': "人生,易如翻掌！　继续前进！",
        'ja': "人生、チョロかった！　続けろ！"
    },
    'life_over': {
        'en': "My life is over!",
        'zh': "我的人生结束了！",
        'ja': "私の人生は終わりました！"
    },
    'deposit_message': {
        'en': "Deposited {amount:.2f} into account. New balance is {balance:.2f}",
        'zh': "存入 {amount:.2f} 到账户。 新余额为 {balance:.2f}",
        'ja': "{amount:.2f} を口座に預け入れました。 新しい残高は {balance:.2f} です"
    },
    'interest_message': {
        'en': "Added {interest:.2f} interest to account. New balance is {balance:.2f}",
        'zh': "账户增加了 {interest:.2f} 的利息。 新余额为 {balance:.2f}",
        'ja': "口座に {interest:.2f} の利息を追加しました。 新しい残高は {balance:.2f} です"
    },
    'withdraw_message': {
        'en': "Withdrew {amount:.2f} from account. New balance is {balance:.2f}",
        'zh': "从账户中提取了 {amount:.2f}。 新余额为 {balance:.2f}",
        'ja': "口座から {amount:.2f} を引き出しました。 新しい残高は {balance:.2f} です"
    },
    'insufficient_balance': {
        'en': "Insufficient balance",
        'zh': "余额不足",
        'ja': "残高不足"
    },
    'yearly_consumption': {
        'en': "age:{age}, monthly cost:{monthly_cost:.2f}, yearly total cost:{total_cost:.2f}, "
              "yearly insurance cost:{insurance_cost:.2f}",
        'zh': "年龄:{age}, 每月费用:{monthly_cost:.2f}, 全年总消费:{total_cost:.2f}, 年保险费用:{insurance_cost:.2f}",
        'ja': "年齢:{age}, 月額:{monthly_cost:.2f}, 年間総消費:{total_cost:.2f}, 年間保険料:{insurance_cost:.2f}"
    },
    'unsupported_language':{
        'en': "Unsupported language!",
        'zh': "不支持的语言!",
        'ja': "サポートされていない言語!"
    },
    "no_exchange_rate": {
        "zh": "没有可用的汇率从 {0} 到 {1}",
        "ja": "{0} から {1} への利用可能な為替レートがありません",
        "en": "No exchange rate available for {0} to {1}"
    },
    "unsupported_type": {
        "zh": "不支持的类型：{0}",
        "ja": "サポートされていない型：{0}",
        "en": "Unsupported type: {0}"
    },
    "division_by_zero": {
        "zh": "不能除以零",
        "ja": "ゼロで割ることはできません",
        "en": "Cannot divide by zero"
    },
    "number_divided_by_money": {
        "zh": "不支持用数字除以Money",
        "ja": "数値を Money で割ることはサポートされていません",
        "en": "Division of a number by Money is not supported"
    },
}


# Function to get translation based on selected language
def get_translation(message_id, lang):
    return translations.get(message_id, {}).get(lang, '')
