translations = {
    'start_message': {
        'en': "Life is easy, start!",
        'zh': "生活,易如反掌！　开始吧！",
        'ja': "人生、チョロかった！　スタート！"
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
        'en': "No.{no}|{year}, age:{age}, monthly cost:{monthly_cost:.2f}, total cost:{total_cost:.2f}, "
              "yearly insurance cost:{insurance_cost:.2f}",
        'zh': "编号.{no}|{year}, 年龄:{age}, 每月费用:{monthly_cost:.2f}, 总消费:{total_cost:.2f}, 年保险费用:{insurance_cost:.2f}",
        'ja': "番号.{no}|{year}, 年齢:{age}, 月額:{monthly_cost:.2f}, 総消費:{total_cost:.2f}, 年間保険料:{insurance_cost:.2f}"
    },
}


# Function to get translation based on selected language
def get_translation(message_id, lang):
    return translations.get(message_id, {}).get(lang, '')
