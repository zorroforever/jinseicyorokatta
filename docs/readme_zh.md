<p align="center">
 <img width="100px" src="/docs/hand-right-outline.svg" align="center" alt="jinseicyorokatta" />
 <h2 align="center">「人生、易如翻掌！」</h2>
 <p align="center">轻松计算您一生的花费，甚至到 100 岁。</p>
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
    <a href="/docs/readme_ja.md">日本語</a>
  </p>
 </p>

## 开始


准备一个正常的 py3.10 环境。

```
apt-get install python
```

## 安装

json文件可以在web上编辑。
执行以下命令。
```
python flask_app.py
```
接着打开浏览器，访问以下网址。
```
http://localhost:5000/
```
<details>
<summary>Web界面翻译</summary>
执行以下命令，
生成.po文件。

> [!NOTE]\
>例：
msgid "Life Configuration"
msgstr "人生设置"
翻译一下。

```
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l zh
```
执行以下命令，
生成.mo文件。
```
pybabel compile -d translations
```
</details>

配置config.json

```
{
    "language": "zh", // 语言
    "currency": "CNY", // 货币
    "mark": "¥", // 货币符号
    "bank_rate": 1.2, // 银行年率
    "initial_balance": 50000000,   // 初期启动资金
    "base_year": 2024, // 开始年
    "years":0, // 经过几年
    "target_year": 2084, // 结束年
    "inflate_rate": 4.48, // 年通胀率
    "birth_year": 1983, // 生日
    "retirement_age": 65, // 退休年龄
    "cost": {
        "monthly": {
            "fixed": {
                "house_fee" :1000,// 住房支出   
                "eng_water_fee" : 50, // 水费
                "eng_electricity_fee" : 200, // 电费
                "eng_gas_fee": 50,// 煤气费
                "eng_network_fee" : 200, // 网费
                "phone_fee" : 200, // 手机费
                "insurance_fee" : 4000 // 保险费
            },
            "variable": {
                "traffic_fee" : 800, // 交通費
                "food_fee" : 3000, // 食費
                "shopping_fee": 3000,// 消费品支出
                "travelling_fee" : 5000,//   旅行费
                "vip_fee" : 400// 各vip会员费
            }
        },
        "annual": {
        }
    }
}

```

monthly.fixed和monthly.variable
可根据您的需要进行设置、
您可以添加其他或删除已有的项目。 

完成设置后，运行以下命令。

```
python life.py path/to/config.json
```
如果是windows、运行以下命令。

```
.\life.exe "path/to/config.json"
```

## 贡献

..

## 版本

..

## 作者

* **haruka.moe** - *Initial work* - [Jinsei Cyorokatta](https://github.com/jinseicyorokatta)


## 许可

该项目的许可证为　GPL v3.0 -  [LICENSE.md](LICENSE.md) 

## 感谢

* 启示
* 其他