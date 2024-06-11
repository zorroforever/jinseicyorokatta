# 「人生、チョロかった！」

「人生、チョロかった！」
簡単に人生を計算し、１００歳になる。

## はじめに

普通のｐｙ３．１０環境を用意してください。

```
apt-get install python
```

### インストール



config.jsonの設定

```
{
    "language": "zh", // 言語設定
    "currency": "CNY", // 通貨設定
    "mark": "¥", // 通貨記号設定
    "bank_rate": 1.2, // 銀行の利率設定
    "initial_balance": 50000000,   // 初期資金設定
    "base_year": 2024, // 基準年設定
    "years":0, // 何年目か設定
    "target_year": 2084, // 目標年設定
    "inflate_rate": 4.48, // 通貨インフレーション率設定
    "birth_year": 1983, // 誕生年設定
    "retirement_age": 65, // 退職年齢設定
    "cost": {
        "monthly": {
            "fixed": {
                "house_fee" :1000,// 家賃   
                "eng_water_fee" : 50, // 水道料金
                "eng_electricity_fee" : 200, // 電気料金
                "eng_gas_fee": 50,// ガス料金
                "eng_network_fee" : 200, // 通信料金
                "phone_fee" : 200, // 電話料金
                "insurance_fee" : 4000 // 保険料金
            },
            "variable": {
                "traffic_fee" : 800, // 交通費
                "food_fee" : 3000, // 食費
                "shopping_fee": 3000,// 買い物料金
                "travelling_fee" : 5000,//   旅費
                "vip_fee" : 400// 各vip会員料金
            }
        },
        "annual": {
        }
    }
}

```

monthly.fixedとmonthly.variableの設定は、  
自分のニーズに合わせて設定してください。  
追加項目を増やしたり、削除したりしても大丈夫です。  

設定を終わったら、以下のコマンドで実行します。

```
python life.py
```


## 貢献

..

## バージョニング

..

## 著者紹介

* **haruka.moe** - *Initial work* - [Jinsei Cyorokatta](https://github.com/jinseicyorokatta)


## ライセンス

このプロジェクトのライセンスは　GPL v3.0 -  [LICENSE.md](LICENSE.md) 

## 謝辞

* インスピレーション
* その他