<p align="center">
 <img width="100px" src="/docs/hand-right-outline.svg" align="center" alt="jinseicyorokatta" />
 <h2 align="center">「Life is easy！」</h2>
 <p align="center">Easily calculate the money you spend in your life and you will be 100 years old.</p>
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
    ·
    <a href="/docs/readme_ja.md">日本語</a>
  </p>
 </p>

## Start


Please prepare a normal py3.10 environment.

```
apt-get install python
```

## Install

setting the config.json

```
{
    "language": "en", // Language 
    "currency": "USD", // Currency 
    "mark": "$", // Currency Symbol
    "bank_rate": 1.2, // Bank interest rate
    "initial_balance": 50000000,   // Initial funding
    "base_year": 2024, // the year start to calculate
    "years":0, // how many years to calculate
    "target_year": 2084, // the year end to calculate
    "inflate_rate": 4.48, // Inflation Rate
    "birth_year": 1983, // birthday
    "retirement_age": 65, // retirement age
    "cost": {
        "monthly": {
            "fixed": {
                "house_fee" :1000,// house_fee   
                "eng_water_fee" : 50, // water fee
                "eng_electricity_fee" : 200, // electricity fee
                "eng_gas_fee": 50,// gas fee
                "eng_network_fee" : 200, // network fee
                "phone_fee" : 200, // phone fee
                "insurance_fee" : 4000 // insurance fee
            },
            "variable": {
                "traffic_fee" : 800, // traffic fee
                "food_fee" : 3000, // food fee
                "shopping_fee": 3000,// shopping fee
                "travelling_fee" : 5000,//  travelling fee
                "vip_fee" : 400// vip fee
            }
        },
        "annual": {
        }
    }
}

```

The monthly.fixed and monthly.variable settings are,  
set according to your own needs.  
You can add or remove additional items.  

When you are done with the settings, run the following command.

```
python life.py path/to/config.json
```


## Contribution

..

## Versioning

..

## Author

* **haruka.moe** - *Initial work* - [Jinsei Cyorokatta](https://github.com/jinseicyorokatta)


## License

The license for this project is　GPL v3.0 -  [LICENSE.md](LICENSE.md) 

## Thanks

* inspiration
* others