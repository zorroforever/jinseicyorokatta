<p align="center">
 <img width="100px" src="/docs/hand-right-outline.svg" align="center" alt="jinseicyorokatta" />
 <h2 align="center">「人生、チョロかった！」</h2>
 <p align="center">簡単に人生の使うお金を計算し、１００歳になる。</p>
 <p align="center">
    <a href="https://github.com/zorroforever/jinseicyorokatta/actions">
      <img alt="Tests Passing" src="/docs/badge.svg" />
    </a>
    <a href="https://github.com/zorroforever/jinseicyorokatta/graphs/contributors">
      <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/zorroforever/jinseicyorokatta" />
    </a>
    <a href="https://github.com/zorroforever/jinseicyorokatta/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/zorroforever/jinseicyorokatta?color=0088ff" />
    </a>
    <a href="https://github.com/zorroforever/jinseicyorokatta/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/zorroforever/jinseicyorokatta?color=0088ff" />
    </a>
    <br />
    <br />
  </p>
 <p align="center">
    <a href="/docs/readme_en.md">English </a>
    ·
    <a href="/docs/readme_zh.md">简体中文</a>
  </p>
 </p>

## はじめに


普通のｐｙ３．１０環境を用意してください。

```
apt-get install python
```


## インストール

webでconfig.jsonの設定することになる。
以下のコマンドで実行します。
```
python flask_app.py
```
それて、ブラウザで以下のURLにアクセスします。

```
http://localhost:5000/
```
<details>
<summary>Webサイトの言語設定</summary>
以下のコマンドで実行します。
poファイルを作成する。

> [!NOTE]\
>例：
msgid "Life Configuration"
msgstr "ライフ設定"
通訳する。

```
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l ja
```
以下のコマンドで実行します。
moファイルを作成する。
```
pybabel compile -d translations
```
</details>

config.jsonの設定

```
{
    "language": "ja", // 言語設定
    "currency": "JPY", // 通貨設定
    "mark": "¥", // 通貨記号設定
    "bank_rate": 0.11, // 銀行の利率設定
    "initial_balance": 500000000,   // 初期資金設定
    "base_year": 2024, // 基準年設定
    "years":0, // 何年目か設定
    "target_year": 2084, // 目標年設定
    "inflate_rate": 4.48, // 通貨インフレーション率設定
    "birth_year": 1983, // 誕生年設定
    "retirement_age": 65, // 退職年齢設定
    "cost": {
        "monthly": {
            "fixed": {
                "house_fee" :100000,// 家賃   
                "eng_water_fee" : 500, // 水道料金
                "eng_electricity_fee" : 2000, // 電気料金
                "eng_gas_fee": 500,// ガス料金
                "eng_network_fee" : 2000, // 通信料金
                "phone_fee" : 2000, // 電話料金
                "insurance_fee" : 40000 // 保険料金
            },
            "variable": {
                "traffic_fee" : 8000, // 交通費
                "food_fee" : 30000, // 食費
                "shopping_fee": 30000,// 買い物料金
                "travelling_fee" : 50000,//   旅費
                "vip_fee" : 4000// 各vip会員料金
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
python life.py path/to/config.json
```
windowsの場合は、以下のコマンドで実行します。

```
.\life.exe "path/to/config.json"
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